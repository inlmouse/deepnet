deepnet
=======
Windows platform executable version of project modified form [DeepNet - OpenHero](https://github.com/OpenHero/deepnet)

## Implementation of some deep learning algorithms. ##

GPU-based python implementation of

1.  Feed-forward Neural Nets
2.  Restricted Boltzmann Machines
3.  Deep Belief Nets
4.  Autoencoders
5.  Deep Boltzmann Machines
6.  Convolutional Neural Nets

Built on top of the [cudamat](http://code.google.com/p/cudamat/) library by
Vlad Mnih and [cuda-convnet](http://code.google.com/p/cuda-convnet/) library by
Alex Krizhevsky.

## Dependencies

- protobuf
- [NumPy](http://www.numpy.org/) 
- Scipy
- [Cudamat](https://github.com/cudamat/cudamat)(already included in this project)
- [CUDA Toolkit 6.0](https://developer.nvidia.com/cuda-toolkit-60)
- [eigen](http://eigen.tuxfamily.org/index.php?title=Main_Page)

## Setup/Configuration

1. Downlaod the eigen library, and put anywhere(eigen_path) you like in your computer(installation is not requiered).
2. Open deepnet.sln in .\deepnet_root by Visual Studio 2012, include your eigen_path into libeigenmat project.
3. Build libcudamat, libcudamat_conv and libeigenmat successively. If successful, 3 dll files will be generated in your .\deepnet_root: libcudamat.dll, libcudamat_conv,dll and libeigenmat.dll. After that, add your .\deepnet_root to OS Environment Variables.
4. Copy folders {eigenmat, cudamat, deepnet} in .\deepnet_root into your_python_root\Lib.
5. Modify IO code in .\deepnet_root\deepnet\util.py(finished).
6. pip install protobuf and NumPy(if nesseary). For protobuf, you may download the codes from [Google Protobuf](https://github.com/google/protobuf).
7. Check your configuration: try import {eigenmat, cudamat, deepnet}.

## Run Example
- Download and extract the MNIST dataset from [MNIST DATASET](http://www.cs.toronto.edu/~nitish/deepnet/mnist.tar.gz), This dataset consists of labelled images of handwritten digits as numpy files.
- cd to the .\deepnet_root\deepnet\examples dir
- Run python setup_examples.py <path to mnist dataset> <output path>. This will modify the example models and trainers to use the specified paths.
- There are examples of different deep learning models. Go to any one and cd to .\deepnet_root\deepnet\examples\rbm and execute "python ../../trainer.py model.pbtxt train.pbtxt eval.pbtxt" in cmd. This should start training an RBM model.

## Acknowledgements
Thanks for OpenHero and HuangHeng's contribution for previous versions of this project.