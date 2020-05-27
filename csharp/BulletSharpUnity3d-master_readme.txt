The files in Assets/Plugins/BulletUnity/BulletSharp and Assets/BulletUnity/Examples/Scenes/BulletSharpDemos are Copyright (c) 2013-2016 Andres Traks. 

This software is provided 'as-is', without any express or implied warranty.
In no event will the authors be held liable for any damages arising from the use of this software.
Permission is granted to anyone to use this software for any purpose,
including commercial applications, and to alter it and redistribute it freely,
subject to the following restrictions:

1. The origin of this software must not be misrepresented; you must not claim that you wrote the original software. If you use this software in a product, an acknowledgment in the product documentation would be appreciated but is not required.
2. Altered source versions must be plainly marked as such, and must not be misrepresented as being the original software.
3. This notice may not be removed or altered from any source distribution.fileFormatVersion: 2
guid: 8c71fd47d8aa69e4e9303425eb398679
timeCreated: 1464398824
licenseType: Free
TextScriptImporter:
  userData: 
  assetBundleName: 
  assetBundleVariant: 
# BulletSharpUnity3d
A fork of the BulletSharp project to make the Bullet Physics Engine usable from C# code in Unity3d
fileFormatVersion: 2
guid: dd5de70bc01bc5d429b234e29899b686
TextScriptImporter:
  externalObjects: {}
  userData: 
  assetBundleName: 
  assetBundleVariant: 
GETTING STARTED WITH BULLET PHYSICS
===================================
INSTALLATION

Bullet Physics For Unity uses unsafe code. There must be a file "smcs.rsp" in the root asset folder that contains:

-unsafe

Sometimes this file is not included

===================================

BULLET UNITY CONTAINS TWO API'S

1) BulletSharp - Located in Plugins/BulletSharp is a low level set of C# wrappers for the native bullet libraries. These wrappers are not integrated with Unity in
any way. Simulations can be run that are not synchronized with Unity's game loop. The demos in BulletUnity/Examples/Scenes/BulletSharpDemos use this API.

2) BulletUnity - Located in BulletUnity/Scripts is a set of Unity Components similar to the PhysX components. These components use the lower level BulletSharp API.

======================
SOURCES OF INFORMATION

The BULLET PHYSICS MANUAL. Download it from the Bullet Physics project on github. It is short (can be read in 1 hour) and will set you up well for working with 
Bullet Physics.

The Bullet Physics Wiki has a lot of good information http://bulletphysics.org/mediawiki-1.5.8/index.php/Main_Page.

The Bullet Physics Forums http://www.bulletphysics.org/Bullet/phpBB3/

The Bullet Physics Examples (ported to C#, then ported to Unity) located in the BulletUnity/Examples/Scenes/BulletSharpDemos folder. More are available in the https://github.com/Phong13/BulletSharpPInvoke project.

DON'T BE AFRAID TO LOOK AT THE BULLET PHYSICS SOURCE CODE. I know it sounds intimidating, but it is much easier than you think. If you are not sure what an API
 call or class does or what a member variable is for, then search for it in the bullet sourcecode. Even if you are not a C++ programmer you can probably deduce
 what it does. I recently spent a few hours on google trying to find good information explaining the difference between btGhostObject and btPairCachingGhostObject.
Eventually I opened the btGhostObject.cpp source file and had a look. The entire sourcecode for both classes is only 170 lines. In about 10 minutes I had a complete
understanding how both classes worked. Much better than an online tutorial.

It is possible to debug from Unity into the Bullet Physics library native code with Visual Studio (probably possible with other IDEs but I havn't tried). To do this you need
to clone the https://github.com/Phong13/BulletSharpPInvoke project. Build a debug, x64 version of libbulletc for windows. Copy the .dll and .pdb file to Unity project (Plugins/Native/x64. 
Then launch Unity from the Visual Studio as described here https://msdn.microsoft.com/en-us/library/605a12zt.aspx.

================================================
IMPORTANT DIFFERENCES WITH UNITY'S PHYSX PHYSICS

Don't try to move the rigid bodies by writing to myRigidBody.transform.position or .rotation. Bullet Physics is not as tightly integrated with Unity as PhysX.
Consider the transform to be completely under the control of Bullet Physics (for non-kinematic RigidBodies) and translate/rotate your rigidBodies using the Bullet Physics API calls.

Be careful of localScale. It is almost completely ignored by Bullet Physics. There are only a few CollisionShapes that can be scaled in the Bullet API (at the time
of writing these have not been implemented in Unity). Modify the shape of the CollisionShape and leave localScale at 1,1,1. You can add your MeshRender as a child of
the CollisionShape and scale that.

Don't try to nest Rigid Bodies. Bullet Unity has no control over the order that bullet updates the transforms of objects each simulation step. If the child RigidBodies get
updated before the parent RigidBodies then the child will jitter terribly.

	WRONG
		RigidBodyGameObjectA
			-RigidBodyGameObjectB
				-RigidBodyGameObjectC

	CORRECT
		RigidBodyGameObjectA
		RigidBodyGameObjectB
		RigidBodyGameObjectC

======================================
FEEL FREE TO CONTRIBUTE TO THE PROJECT

Bullet Unity is an open source project in GitHub. Please feel free to clone the github repository and contribute:

	https://github.com/Phong13/BulletUnity
	https://github.com/Phong13/BulletSharpPInvoke



  fileFormatVersion: 2
guid: 30388b92f282cc34994eaa5be83b8cb5
timeCreated: 1456287928
licenseType: Free
TextScriptImporter:
  userData: 
  assetBundleName: 
  assetBundleVariant: 
This version of the libbulletc library requires Unity 5.3.4 or higher.

Building for Universal Windows Platform generates errors about unsafe code. The presence of -unsafe in the SMCP.rsp file is supposed to allow unsafe code
but does not seem to work on Universal Windows Platform.

A workaround is to compile the code in: /Plugins/BulletUnity/BulletSharp into a .dll and include that in the project instead of the C# files.fileFormatVersion: 2
guid: 508b42418ba4d944ab90c02ebf069371
timeCreated: 1475198292
licenseType: Free
TextScriptImporter:
  userData: 
  assetBundleName: 
  assetBundleVariant: 
INCLUDE_DIRECTORIES(
	${BULLET_PHYSICS_SOURCE_DIR}/src
	${BULLET_PHYSICS_SOURCE_DIR}/Extras/Serialize/BulletFileLoader
)

ADD_LIBRARY(
BulletWorldImporter
btBulletWorldImporter.cpp
btBulletWorldImporter.h
btWorldImporter.cpp
btWorldImporter.h
)

SET_TARGET_PROPERTIES(BulletWorldImporter PROPERTIES VERSION ${BULLET_VERSION})
SET_TARGET_PROPERTIES(BulletWorldImporter PROPERTIES SOVERSION ${BULLET_VERSION})

IF (BUILD_SHARED_LIBS)
	TARGET_LINK_LIBRARIES(BulletWorldImporter BulletDynamics BulletCollision BulletFileLoader LinearMath)
ENDIF (BUILD_SHARED_LIBS)

IF (INSTALL_EXTRA_LIBS)
	IF (NOT INTERNAL_CREATE_DISTRIBUTABLE_MSVC_PROJECTFILES)
		#FILES_MATCHING requires CMake 2.6
		IF (${CMAKE_MAJOR_VERSION}.${CMAKE_MINOR_VERSION} GREATER 2.5)
			IF (APPLE AND BUILD_SHARED_LIBS AND FRAMEWORK)
				INSTALL(TARGETS BulletWorldImporter DESTINATION .)
			ELSE (APPLE AND BUILD_SHARED_LIBS AND FRAMEWORK)
				INSTALL(TARGETS BulletWorldImporter DESTINATION lib${LIB_SUFFIX})
				INSTALL(DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
DESTINATION ${INCLUDE_INSTALL_DIR} FILES_MATCHING PATTERN "*.h"  PATTERN
".svn" EXCLUDE PATTERN "CMakeFiles" EXCLUDE)
			ENDIF (APPLE AND BUILD_SHARED_LIBS AND FRAMEWORK)
		ENDIF (${CMAKE_MAJOR_VERSION}.${CMAKE_MINOR_VERSION} GREATER 2.5)

		IF (APPLE AND BUILD_SHARED_LIBS AND FRAMEWORK)
			SET_TARGET_PROPERTIES(BulletWorldImporter PROPERTIES FRAMEWORK true)
			SET_TARGET_PROPERTIES(BulletWorldImporter PROPERTIES PUBLIC_HEADER "btBulletWorldImporter.h")
		ENDIF (APPLE AND BUILD_SHARED_LIBS AND FRAMEWORK)
	ENDIF (NOT INTERNAL_CREATE_DISTRIBUTABLE_MSVC_PROJECTFILES)
ENDIF (INSTALL_EXTRA_LIBS)
nDispatch/btSphereSphereCollisionAlgorithm.cpp
	CollisionDispatch/btSphereTriangleCollisionAlgorithm.cpp
	CollisionDispatch/btUnionFind.cpp
	CollisionDispatch/SphereTriangleDetector.cpp
	CollisionShapes/btBoxShape.cpp
	CollisionShapes/btBox2dShape.cpp
	CollisionShapes/btBvhTriangleMeshShape.cpp
	CollisionShapes/btCapsuleShape.cpp
	CollisionShapes/btCollisionShape.cpp
	CollisionShapes/btCompoundShape.cpp
	CollisionShapes/btConcaveShape.cpp
	CollisionShapes/btConeShape.cpp
	CollisionShapes/btConvexHullShape.cpp
	CollisionShapes/btConvexInternalShape.cpp
	CollisionShapes/btConvexPointCloudShape.cpp
	CollisionShapes/btConvexPolyhedron.cpp
	CollisionShapes/btConvexShape.cpp
	CollisionShapes/btConvex2dShape.cpp
	CollisionShapes/btConvexTriangleMeshShape.cpp
	CollisionShapes/btCylinderShape.cpp
	CollisionShapes/btEmptyShape.cpp
	CollisionShapes/btHeightfieldTerrainShape.cpp
	CollisionShapes/btMinkowskiSumShape.cpp
	CollisionShapes/btMultimaterialTriangleMeshShape.cpp
	CollisionShapes/btMultiSphereShape.cpp
	CollisionShapes/btOptimizedBvh.cpp
	CollisionShapes/btPolyhedralConvexShape.cpp
	CollisionShapes/btScaledBvhTriangleMeshShape.cpp
	CollisionShapes/btShapeHull.cpp
	CollisionShapes/btSphereShape.cpp
	CollisionShapes/btStaticPlaneShape.cpp
	CollisionShapes/btStridingMeshInterface.cpp
	CollisionShapes/btTetrahedronShape.cpp
	CollisionShapes/btTriangleBuffer.cpp
	CollisionShapes/btTriangleCallback.cpp
	CollisionShapes/btTriangleIndexVertexArray.cpp
	CollisionShapes/btTriangleIndexVertexMaterialArray.cpp
	CollisionShapes/btTriangleMesh.cpp
	CollisionShapes/btTriangleMeshShape.cpp
	CollisionShapes/btUniformScalingShape.cpp
	Gimpact/btContactProcessing.cpp
	Gimpact/btGenericPoolAllocator.cpp
	Gimpact/btGImpactBvh.cpp
	Gimpact/btGImpactCollisionAlgorithm.cpp
	Gimpact/btGImpactQuantizedBvh.cpp
	Gimpact/btGImpactShape.cpp
	Gimpact/btTriangleShapeEx.cpp
	Gimpact/gim_box_set.cpp
	Gimpact/gim_contact.cpp
	Gimpact/gim_memory.cpp
	Gimpact/gim_tri_collision.cpp
	NarrowPhaseCollision/btContinuousConvexCollision.cpp
	NarrowPhaseCollision/btConvexCast.cpp
	NarrowPhaseCollision/btGjkConvexCast.cpp
	NarrowPhaseCollision/btGjkEpa2.cpp
	NarrowPhaseCollision/btGjkEpaPenetrationDepthSolver.cpp
	NarrowPhaseCollision/btGjkPairDetector.cpp
	NarrowPhaseCollision/btMinkowskiPenetrationDepthSolver.cpp
	NarrowPhaseCollision/btPersistentManifold.cpp
	NarrowPhaseCollision/btRaycastCallback.cpp
	NarrowPhaseCollision/btSubSimplexConvexCast.cpp
	NarrowPhaseCollision/btVoronoiSimplexSolver.cpp
	NarrowPhaseCollision/btPolyhedralContactClipping.cpp
)

SET(Root_HDRS
	../btBulletCollisionCommon.h
)
SET(BroadphaseCollision_HDRS
	BroadphaseCollision/btAxisSweep3.h
	BroadphaseCollision/btBroadphaseInterface.h
	BroadphaseCollision/btBroadphaseProxy.h
	BroadphaseCollision/btCollisionAlgorithm.h
	BroadphaseCollision/btDbvt.h
	BroadphaseCollision/btDbvtBroadphase.h
	BroadphaseCollision/btDispatcher.h
	BroadphaseCollision/btMultiSapBroadphase.h
	BroadphaseCollision/btOverlappingPairCache.h
	BroadphaseCollision/btOverlappingPairCallback.h
	BroadphaseCollision/btQuantizedBvh.h
	BroadphaseCollision/btSimpleBroadphase.h
)
SET(CollisionDispatch_HDRS
	CollisionDispatch/btActivatingCollisionAlgorithm.h
	CollisionDispatch/btBoxBoxCollisionAlgorithm.h
	CollisionDispatch/btBox2dBox2dCollisionAlgorithm.h
	CollisionDispatch/btBoxBoxDetector.h
	CollisionDispatch/btCollisionConfiguration.h
	CollisionDispatch/btCollisionCreateFunc.h
	CollisionDispatch/btCollisionDispatcher.h
	CollisionDispatch/btCollisionObject.h
	CollisionDispatch/btCollisionObjectWrapper.h
	CollisionDispatch/btCollisionWorld.h
	CollisionDispatch/btCollisionWorldImporter.h
	CollisionDispatch/btCompoundCollisionAlgorithm.h
	CollisionDispatch/btCompoundCompoundCollisionAlgorithm.h
	CollisionDispatch/btConvexConcaveCollisionAlgorithm.h
	CollisionDispatch/btConvexConvexAlgorithm.h
	CollisionDispatch/btConvex2dConvex2dAlgorithm.h
	CollisionDispatch/btConvexPlaneCollisionAlgorithm.h
	CollisionDispatch/btDefaultCollisionConfiguration.h
	CollisionDispatch/btEmptyCollisionAlgorithm.h
	CollisionDispatch/btGhostObject.h
	CollisionDispatch/btHashedSimplePairCache.h
	CollisionDispatch/btManifoldResult.h
	CollisionDispatch/btSimulationIslandManager.h
	CollisionDispatch/btSphereBoxCollisionAlgorithm.h
	CollisionDispatch/btSphereSphereCollisionAlgorithm.h
	CollisionDispatch/btSphereTriangleCollisionAlgorithm.h
	CollisionDispatch/btUnionFind.h
	CollisionDispatch/SphereTriangleDetector.h
)
SET(CollisionShapes_HDRS
	CollisionShapes/btBoxShape.h
	CollisionShapes/btBox2dShape.h
	CollisionShapes/btBvhTriangleMeshShape.h
	CollisionShapes/btCapsuleShape.h
	CollisionShapes/btCollisionMargin.h
	CollisionShapes/btCollisionShape.h
	CollisionShapes/btCompoundShape.h
	CollisionShapes/btConcaveShape.h
	CollisionShapes/btConeShape.h
	CollisionShapes/btConvexHullShape.h
	CollisionShapes/btConvexInternalShape.h
	CollisionShapes/btConvexPointCloudShape.h
	CollisionShapes/btConvexPolyhedron.h
	CollisionShapes/btConvexShape.h
	CollisionShapes/btConvex2dShape.h
	CollisionShapes/btConvexTriangleMeshShape.h
	CollisionShapes/btCylinderShape.h
	CollisionShapes/btEmptyShape.h
	CollisionShapes/btHeightfieldTerrainShape.h
	CollisionShapes/btMaterial.h
	CollisionShapes/btMinkowskiSumShape.h
	CollisionShapes/btMultimaterialTriangleMeshShape.h
	CollisionShapes/btMultiSphereShape.h
	CollisionShapes/btOptimizedBvh.h
	CollisionShapes/btPolyhedralConvexShape.h
	CollisionShapes/btScaledBvhTriangleMeshShape.h
	CollisionShapes/btShapeHull.h
	CollisionShapes/btSphereShape.h
	CollisionShapes/btStaticPlaneShape.h
	CollisionShapes/btStridingMeshInterface.h
	CollisionShapes/btTetrahedronShape.h
	CollisionShapes/btTriangleBuffer.h
	CollisionShapes/btTriangleCallback.h
	CollisionShapes/btTriangleIndexVertexArray.h
	CollisionShapes/btTriangleIndexVertexMaterialArray.h
	CollisionShapes/btTriangleInfoMap.h
	CollisionShapes/btTriangleMesh.h
	CollisionShapes/btTriangleMeshShape.h
	CollisionShapes/btTriangleShape.h
	CollisionShapes/btUniformScalingShape.h
)
SET(Gimpact_HDRS
	Gimpact/btBoxCollision.h
	Gimpact/btClipPolygon.h
	Gimpact/btContactProcessing.h
	Gimpact/btGenericPoolAllocator.h
	Gimpact/btGeometryOperations.h
	Gimpact/btGImpactBvh.h
	Gimpact/btGImpactCollisionAlgorithm.h
	Gimpact/btGImpactMassUtil.h
	Gimpact/btGImpactQuantizedBvh.h
	Gimpact/btGImpactShape.h
	Gimpact/btQuantization.h
	Gimpact/btTriangleShapeEx.h
	Gimpact/gim_array.h
	Gimpact/gim_basic_geometry_operations.h
	Gimpact/gim_bitset.h
	Gimpact/gim_box_collision.h
	Gimpact/gim_box_set.h
	Gimpact/gim_clip_polygon.h
	Gimpact/gim_contact.h
	Gimpact/gim_geom_types.h
	Gimpact/gim_geometry.h
	Gimpact/gim_hash_table.h
	Gimpact/gim_linear_math.h
	Gimpact/gim_math.h
	Gimpact/gim_memory.h
	Gimpact/gim_radixsort.h
	Gimpact/gim_tri_collision.h
)
SET(NarrowPhaseCollision_HDRS
	NarrowPhaseCollision/btContinuousConvexCollision.h
	NarrowPhaseCollision/btConvexCast.h
	NarrowPhaseCollision/btConvexPenetrationDepthSolver.h
	NarrowPhaseCollision/btDiscreteCollisionDetectorInterface.h
	NarrowPhaseCollision/btGjkConvexCast.h
	NarrowPhaseCollision/btGjkEpa2.h
	NarrowPhaseCollision/btGjkEpaPenetrationDepthSolver.h
	NarrowPhaseCollision/btGjkPairDetector.h
	NarrowPhaseCollision/btManifoldPoint.h
	NarrowPhaseCollision/btMinkowskiPenetrationDepthSolver.h
	NarrowPhaseCollision/btPersistentManifold.h
	NarrowPhaseCollision/btPointCollector.h
	NarrowPhaseCollision/btRaycastCallback.h
	NarrowPhaseCollision/btSimplexSolverInterface.h
	NarrowPhaseCollision/btSubSimplexConvexCast.h
	NarrowPhaseCollision/btVoronoiSimplexSolver.h
	NarrowPhaseCollision/btPolyhedralContactClipping.h
)

SET(BulletCollision_HDRS
	${Root_HDRS}
	${BroadphaseCollision_HDRS}
	${CollisionDispatch_HDRS}
	${CollisionShapes_HDRS}
	${Gimpact_HDRS}
	${NarrowPhaseCollision_HDRS}
)


ADD_LIBRARY(BulletCollision ${BulletCollision_SRCS} ${BulletCollision_HDRS})
SET_TARGET_PROPERTIES(BulletCollision PROPERTIES VERSION ${BULLET_VERSION})
SET_TARGET_PROPERTIES(BulletCollision PROPERTIES SOVERSION ${BULLET_VERSION})
IF (BUILD_SHARED_LIBS)
  TARGET_LINK_LIBRARIES(BulletCollision LinearMath)
ENDIF (BUILD_SHARED_LIBS)


IF (INSTALL_LIBS)
	IF (NOT INTERNAL_CREATE_DISTRIBUTABLE_MSVC_PROJECTFILES)
		#INSTALL of other files requires CMake 2.6
		IF (${CMAKE_MAJOR_VERSION}.${CMAKE_MINOR_VERSION} GREATER 2.5)
			IF (APPLE AND BUILD_SHARED_LIBS AND FRAMEWORK)
				INSTALL(TARGETS BulletCollision DESTINATION .)
			ELSE (APPLE AND BUILD_SHARED_LIBS AND FRAMEWORK)
				INSTALL(TARGETS BulletCollision RUNTIME DESTINATION bin
								LIBRARY DESTINATION lib${LIB_SUFFIX}
								ARCHIVE DESTINATION lib${LIB_SUFFIX})
				INSTALL(DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
DESTINATION ${INCLUDE_INSTALL_DIR} FILES_MATCHING PATTERN "*.h" PATTERN ".svn" EXCLUDE PATTERN "CMakeFiles" EXCLUDE)
				INSTALL(FILES ../btBulletCollisionCommon.h
DESTINATION ${INCLUDE_INSTALL_DIR}/BulletCollision)
			ENDIF (APPLE AND BUILD_SHARED_LIBS AND FRAMEWORK)
		ENDIF (${CMAKE_MAJOR_VERSION}.${CMAKE_MINOR_VERSION} GREATER 2.5)

		IF (APPLE AND BUILD_SHARED_LIBS AND FRAMEWORK)
			SET_TARGET_PROPERTIES(BulletCollision PROPERTIES FRAMEWORK true)

			SET_TARGET_PROPERTIES(BulletCollision PROPERTIES PUBLIC_HEADER "${Root_HDRS}")
			# Have to list out sub-directories manually:
			SET_PROPERTY(SOURCE ${BroadphaseCollision_HDRS} PROPERTY MACOSX_PACKAGE_LOCATION Headers/BroadphaseCollision)
			SET_PROPERTY(SOURCE ${CollisionDispatch_HDRS} PROPERTY MACOSX_PACKAGE_LOCATION Headers/CollisionDispatch)
			SET_PROPERTY(SOURCE ${CollisionShapes_HDRS} PROPERTY MACOSX_PACKAGE_LOCATION Headers/CollisionShapes)
			SET_PROPERTY(SOURCE ${Gimpact_HDRS} PROPERTY MACOSX_PACKAGE_LOCATION Headers/Gimpact)
			SET_PROPERTY(SOURCE ${NarrowPhaseCollision_HDRS} PROPERTY MACOSX_PACKAGE_LOCATION Headers/NarrowPhaseCollision)

		ENDIF (APPLE AND BUILD_SHARED_LIBS AND FRAMEWORK)
	ENDIF (NOT INTERNAL_CREATE_DISTRIBUTABLE_MSVC_PROJECTFILES)
ENDIF (INSTALL_LIBS)
