import InMemoryModel as IMM
import ModelElements as ME

if __name__ == '__main__':
    observer1 = IMM.Observer("server1")
    observer2 = IMM.Observer("server2")

    poligons = ME.Poligon([ME.Point3D(1,2,3)])
    poligonalModel = ME.PoligonalModel([poligons])
    models = [poligonalModel]

    angel3D = ME.Angle3D(ME.Vector3D(ME.Point3D(3,4,5),ME.Point3D(2,4,6)),ME.Vector3D(ME.Point3D(3,3,5),ME.Point3D(2,2,6)))

    scene = ME.Scene(poligonalModel,ME.Camera(ME.Point3D(3,2,1),angel3D))
    scenes = [scene]

    flashes = [ME.Flash(ME.Point3D(4,5,6),angel3D,ME.Color(23,45,67),34)]

    cameras = [ME.Camera(ME.Point3D(4,6,9),angel3D)]

    model_store = IMM.ModelStore(models, scenes, flashes, cameras)

    model_store.registerModelChanger(observer2)
    model_store.registerModelChanger(observer1)

    model_store.addModel(poligonalModel)
    model_store.removeModel(poligonalModel)