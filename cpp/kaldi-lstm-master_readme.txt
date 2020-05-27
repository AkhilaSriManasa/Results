# LSTM-projected BPTT in Kaldi nnet1
## Diagram
![Diagram](https://raw.githubusercontent.com/dophist/kaldi-lstm/master/misc/LSTM_DIAG_EQUATION.jpg)

## Notes:  
* peephole connection(purple) are diagonal
* output-gate peephole is not recursive
* dashed arrows: adaptive weight, i.e activations of (input gate, forget gate, output gate)

Currently implementation includes two versions:
* standard
* google

Go to sub-directory to get more details.

# FAQ
## Q1. How to decode with LSTM?
* Standard version: exactly the same as DNN, feed LSTM nnet into nnet-forward as AM scorer, remember nnet-forward doesn't have a mechanism to delay target, so "time-shift" component is needed to do this.
* Google version: 
	- convert binary nnet into text format via nnet-copy, and open text nnet with your text editor
	- change "Transmit" component to "TimeShift", keep your <Shift> setup consistent with "--targets-delay" used in nnet-train-lstm-streams
	- edit "LstmProjectedStreams" to "LstmProjected", remove "NumStream" tag, now the "google version" is converted to "standard version", and you can perform AM scoring via nnet-forward, e.g:
```
<Nnet>
<TimeShift> 40 40 <Shift> 5
<LstmProjected> 512 40 <CellDim> 800 [ ...
<AffineTransform> 16624 512 <LearnRateCoef> 1 <BiasLearnRateCoef> 1 <MaxNorm> 0  [ ...
<Softmax> 16624 16624
</Nnet>
```

## Q2. How do I stack more than one layer of LSTM?
In google's paper, two layers of medium-sized LSTM is the best setup to beat DNN on WER. You can do this by text level editing:
* use some of your training data to train one layer LSTM nnet
* convert it into text format with nnet-copy with "--binary=false"
* insert a pre-initialized LSTM component text between softmax and your pretrained LSTM, and you can feed all your training data to the stacked LSTM, e.g:
```
<Nnet>
<Transmit> 40 40
<LstmProjectedStreams> 512 40 <CellDim> 800 <NumStream> 4  [ ...
<LstmProjectedStreams> 512 512 <CellDim> 800 <NumStream> 4  [ ...
<AffineTransform> 16624 512 <LearnRateCoef> 1 <BiasLearnRateCoef> 1 <MaxNorm> 0  [ ...
<Softmax> 16624 16624
</Nnet>
```
## Q3. How do I know when to use "Transmit" or "TimeShift"?
The key is how you apply "target-delay".  
* standard version: the nnet should be trained with "TimeShift" because default nnet1 training tool (nnet-train-frame-shuf & nnet-train-perutt) doesn't provide target delay. 
* google version: due to the complexity of multi-stream training, the training tool "nnet-train-lstm-streams" provides an option "--target-delay", so in multi-stream training, a dummy "Transmit" component is used for a trivial reason related to how nnet1 calls Backpropagate(). But in testing time, the google version is first converted to standard version, so the "transmit" should also be switched to "TimeShift" during the conversion.

## Q4. Why are the "dropout" codes commented out?
I implemented the "forward-connection droping out" according another paper from google, but later I didn't implement dropout retention, so the effects of dropout are not tested at all, and I leave it commented out.
<Nnet> 
<AddShift> 40 40
 [ -17.079094 -18.330235 -18.892422 -19.260805 -19.341509 -19.143805 -19.025459 -18.584808 -18.794634 -18.655685 -18.513309 -18.192837 -17.995968 -17.756639 -17.635500 -17.518309 -17.366745 -17.175817 -16.950079 -16.773527 -16.513748 -16.351526 -16.239607 -16.173403 -16.147905 -16.146242 -16.067930 -15.899789 -15.696648 -15.543466 -15.428617 -15.434534 -15.447815 -15.395354 -15.327708 -15.339854 -15.392885 -15.266589 -15.167926 -15.163923 ]
<Rescale> 40 40
 [ 0.274377 0.268400 0.265746 0.260280 0.255437 0.255657 0.257957 0.255230 0.253199 0.251413 0.251958 0.254203 0.256505 0.259011 0.261760 0.265216 0.269026 0.272476 0.275385 0.278205 0.280523 0.282497 0.284788 0.286656 0.287739 0.289117 0.290843 0.293312 0.295994 0.298431 0.300347 0.301902 0.302388 0.301528 0.299186 0.296792 0.295728 0.296119 0.296952 0.296109 ]
</Nnet> 
# google's multi-stream version
For architecture details, read Google papers in this directory.

notable modifications to standard LSTM training includes:
### batched-BPTT
As a special case to williams' BPTT(h,h-prime), Google uses a "batched" BPTT (Tbptt=20), this avoids the BPTT time-expension from being too deep, the gradients are less likely to blow up, hence greatly improves training stability in large data set.
Inside an utterance, network states of previous batch are saved as history states and bridged into the next batch.

### multi-stream training
Multiple utterances are processed simultaneously(4 utterances per CPU in Google's setup). 

I prefer the term "multi-stream" training
* greatly speed up the training.
* add sample-level stochasticity, which is benefical in SGD.

To elaborate the second point: epoch-wise BPTT shuffles the training data in utterance level, whereas frame-level stochasticity is missing due to the sequential nature of all RNN trainign algorithms. However, multi-stream training receives updates from different utterances at the same time, which improves stochasticity.

The core LSTM algorithms are implemented in nnet/bd-nnet-lstm-projected-streams.h

To speed up the training and get rid of unnecessary matrix buffers, two methods are added to Matrix & CuMatrix:
* AddMatDiagVec() 
* AddMatDotMat()

for more details, see codes in matrix/kaldi-matrix.{h.cc} & cudamatrix/cu-matrix.{h,cc}

Due to the complexity of multi-stream training, a new eval method is added:
* Xent::EvalMasked()

for more details, see codes in nnet/nnet-loss.{h.cc}

# standard version
* Standard LSTM implementation, using epoch-wise BPTT training algorithm, one utterance a time.
* it is now completely compatible with nnet1 codes:
	- you can simple add the lstm component into nnet-component.{h.cc} as usual, just as simple as that
	- you can train Cross-Entropy model with nnet-train-perutt
	- you can do discriminative sequential training(MMI/MPE/sMBR) with nnet-train-mmi-sequential/nnet-train-mpe-sequential

Try it out.

## Targets Delay
Note that in speech recognition, future acoustic context can be beneficial for system performance: DNN achieves this by splicing both left and right neighbouring frames; In LSTM-RNN, this can be done by delaying the targets(typically by 5).
So I also provide a "pre-processing" time-shift component to achieve targets delay, by advancing the features by 5 frames, see the code for details.

## TODO
* bi-directional LSTM  
* Now both vector and matrix representations are used mixed for computation, seems a little redundent. May add DiffSigmoid, DiffTanh to CuVector to clean it up.
