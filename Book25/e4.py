from cStringIO import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
def convert(fname, pages=None):
    if not pages:
        pagenums = set()
    else:
        pagenums = set(pages)

    output = StringIO()
    manager = PDFResourceManager()
    converter = TextConverter(manager, output, laparams=LAParams())
    interpreter = PDFPageInterpreter(manager, converter)

    infile = file(fname, 'rb')
    for page in PDFPage.get_pages(infile, pagenums):
        interpreter.process_page(page)
    infile.close()
    converter.close()
    text = output.getvalue()
    output.close
    return text

l1 = [['basis'], ['grid'], ['grid'], ['smoothing'], ['Adjoint', 'operator'], ['frame'], ['Admissible', 'tree'], ['Admissible', 'tree'], ['Admissible', 'tree'], ['Admissible', 'tree'], ['Af\xef\xac\x81ne', 'invariance'], ['Algorithme', '\xc3\xa0', 'trous'], ['Algorithme', '\xc3\xa0', 'trous'], ['Aliasing'], ['Aliasing'], ['Aliasing'], ['Aliasing'], ['Ambiguity', 'function'], ['Ambiguity', 'function'], ['Amplitude', 'modulation'], ['Amplitude', 'modulation'], ['Analog', 'digital', 'conversion'], ['Analog', 'digital', 'conversion'], ['Analog', 'digital', 'conversion'], ['168'], ['discrete', 'signal'], ['discrete', 'signal'], ['function'], ['function'], ['wavelet'], ['wavelet'], ['adaptive', 'grid'], ['bounded', 'variation'], ['bounded', 'variation'], ['image'], ['in', 'wavelet', 'bases'], ['in', 'wavelet', 'bases'], ['linear'], ['linear'], ['linear'], ['linear'], ['linear'], ['nonlinear'], ['nonlinear'], ['nonlinear'], ['nonlinear'], ['support'], ['support'], ['support'], ['support'], ['thresholding'], ['uniform', 'grid'], ['Arithmetic', 'code'], ['Arithmetic', 'code'], ['Arithmetic', 'code'], ['510'], ['time-frequency'], ['time-frequency'], ['wavelet'], ['wavelet'], ['wavelet'], ['windowed', 'Fourier'], ['masking'], ['scaling'], ['scaling'], ['scaling'], ['transposition'], ['transposition'], ['transposition'], ['Backprojection'], ['l1', 'pursuit'], ['matching', 'pursuit'], ['Radon'], ['Balian-Low', 'theorem'], ['Balian-Low', 'theorem'], ['Banach', 'space'], ['Bandlets'], ['biorthogonal'], ['biorthogonal'], ['biorthogonal'], ['biorthogonal'], ['orthogonal'], ['pursuit'], ['Riesz'], ['Riesz'], ['Riesz'], ['Basis', 'pursuit'], ['Lagragian'], ['Lagragian'], ['Lagragian'], ['Lagragian'], ['wavelet', 'packets'], ['Battle-Lemari\xc3\xa9', 'wavelet'], ['Battle-Lemari\xc3\xa9', 'wavelet'], ['Battle-Lemari\xc3\xa9', 'wavelet'], ['estimation'], ['estimation'], ['estimation'], ['risk'], ['risk'], ['risk'], ['Bernouilli', 'random', 'matrix'], ['Bernstein', 'inequality'], ['norm'], ['space'], ['space'], ['space'], ['Best', 'approximation'], ['Best', 'basis'], ['Best', 'basis'], ['Best', 'basis'], ['Best', 'basis'], ['approximation'], ['compression'], ['local', 'cosine'], ['search'], ['wavelet', 'packet'], ['Bezout', 'theorem'], ['Bezout', 'theorem'], ['Binary', 'tree'], ['basis'], ['fast', 'transform'], ['lifting'], ['ordering'], ['regularity'], ['splines'], ['splines'], ['support'], ['symmetry'], ['symmetry'], ['two-dimensional'], ['vanishing', 'moments'], ['Blind', 'source', 'separation'], ['Block', 'basis'], ['Block', 'basis'], ['cosine'], ['cosine'], ['Fourier'], ['two-dimensional'], ['Block', 'thresholding'], ['risk'], ['Boundary', 'conditions'], ['Boundary', 'conditions'], ['Boundary', 'wavelets'], ['Boundary', 'wavelets'], ['Boundary', 'wavelets'], ['discrete', 'signal'], ['function'], ['function'], ['function'], ['function'], ['function'], ['function'], ['601'], ['image'], ['image'], ['image'], ['image'], ['image'], ['Box', 'spline'], ['Box', 'spline'], ['Box', 'spline'], ['Butterworth', '\xef\xac\x81lter'], ['Canny', 'edge', 'detector'], ['measure'], ['set'], ['spectrum'], ['Capacity', 'dimension'], ['CART', 'algorithm'], ['Cartoon', 'image'], ['Cauchy-Schwarz', 'inequality'], ['Chambolle', 'algorithm'], ['Channel', 'coding'], ['hyperbolic'], ['hyperbolic'], ['linear'], ['linear'], ['linear'], ['quadratic'], ['Choi-William', 'distribution'], ['Co-area', 'formula'], ['Coarse', 'to', '\xef\xac\x81ne'], ['adaptive'], ['adaptive'], ['arithmetic'], ['block'], ['conditional'], ['embedded'], ['embedded'], ['Huffman'], ['pre\xef\xac\x81x'], ['Shannon'], ['variable', 'length'], ['variable', 'length'], ['Coding', 'gain'], ['Cohen\xe2\x80\x99s', 'class'], ['discrete'], ['marginals'], ['matching', 'pursuit'], ['structure'], ['Coi\xef\xac\x82ets'], ['Color', 'image(s)'], ['Color', 'image(s)'], ['Color', 'image(s)'], ['Compact', 'support'], ['Compact', 'support'], ['Compact', 'support'], ['audio'], ['dictionary'], ['image'], ['image'], ['speech'], ['video'], ['video'], ['Compressive', 'sensing'], ['Compressive', 'sensing'], ['Concave', 'function'], ['Concentration', 'inequality'], ['Conditional', 'expectation'], ['Cone', 'of', 'in\xef\xac\x82uence'], ['Cone', 'of', 'in\xef\xac\x82uence'], ['Conjugate', 'gradient'], ['Conjugate', 'mirror', '\xef\xac\x81lters'], ['Conjugate', 'mirror', '\xef\xac\x81lters'], ['276'], ['choice'], ['choice'], ['Daubechies'], ['Smith-Barnwell'], ['Vaidyanath-Hoang'], ['function'], ['hull'], ['hull'], ['hull'], ['quadratic'], ['circular'], ['circular'], ['circular'], ['circular'], ['circular'], ['circular'], ['450'], ['continuous'], ['discrete'], ['fast', 'FFT', 'algorithm'], ['fast', 'overlap\xe2\x80\x93add'], ['integral'], ['separable'], ['circular'], ['discrete'], ['Fourier', 'integral'], ['Cosine', 'I', 'basis'], ['Cosine', 'I', 'basis'], ['Cosine', 'I', 'basis'], ['discrete'], ['discrete'], ['Cosine', 'IV', 'basis'], ['Cosine', 'IV', 'basis'], ['discrete'], ['discrete'], ['Cost', 'function'], ['Covariance'], ['Covariance'], ['operator'], ['operator'], ['operator'], ['Cubic', 'spline'], ['Cubic', 'spline'], ['Curvelets'], ['Curvelets'], ['denoising'], ['tight', 'frame'], ['Daubechies', 'wavelets'], ['DCT-I'], ['DCT-I'], ['DCT-IV'], ['DCT-IV'], ['Decibels'], ['Decibels'], ['Deinterlacing'], ['Devil\xe2\x80\x99s', 'staircases'], ['Dictionary'], ['denoising'], ['Gabor'], ['local', 'cosine'], ['local', 'cosine'], ['orthonormal', 'bases'], ['wavelet', 'packet'], ['wavelet', 'packet'], ['Dirac'], ['Dirac'], ['Dirac'], ['Dirac'], ['Dirac'], ['comb'], ['comb'], ['comb'], ['Discrete', 'Fourier', 'transform'], ['Discrete', 'Fourier', 'transform'], ['Discrete', 'Fourier', 'transform'], ['inversion'], ['Plancherel', 'formula'], ['two-dimensional'], ['Discrete', 'wavelet', 'basis'], ['Discrete', 'wavelet', 'basis'], ['Distortion', 'rate'], ['Distortion', 'rate'], ['Distortion', 'rate'], ['Distortion', 'rate'], ['Dolby'], ['Dominated', 'convergence'], ['Dominated', 'convergence'], ['analysis'], ['frame'], ['synthesis'], ['synthesis'], ['Dyadic', 'wavelet', 'transform'], ['Dyadic', 'wavelet', 'transform'], ['Dyadic', 'wavelet', 'transform'], ['maxima'], ['splines'], ['two-dimensional'], ['curve'], ['curve'], ['detection'], ['illusory'], ['image', 'reconstruction'], ['image', 'reconstruction'], ['multiscales'], ['Eigenvector'], ['Eigenvector'], ['Eigenvector'], ['Embedded', 'code'], ['Embedded', 'code'], ['discrete', 'Fourier', 'transform'], ['discrete', 'windowed', 'Fourier'], ['Fourier', 'integral'], ['Fourier', 'series'], ['matching', 'pursuit'], ['tight', 'frame'], ['wavelet', 'transform'], ['wavelet', 'transform'], ['windowed', 'Fourier'], ['Entropy'], ['differential'], ['Error', 'correcting', 'code'], ['Estimation'], ['adaptive'], ['block', 'thresholding'], ['multiscale', 'edges'], ['noise', 'variance'], ['oracle'], ['oracle'], ['oracle'], ['oracle'], ['orthogonal', 'projection'], ['thresholding'], ['Wiener'], ['Exact', 'Recovery', 'Criteria'], ['Exact', 'Recovery', 'Criteria'], ['Fast', 'Fourier', 'transform'], ['two-dimensional'], ['biorthogonal'], ['continuous'], ['dyadic'], ['initialization'], ['multidimensional'], ['orthogonal'], ['two-dimensional'], ['Fatou', 'lemma'], ['Filter'], ['analog'], ['causal'], ['causal'], ['discrete'], ['interpolation'], ['low-pass'], ['low-pass'], ['recursive', 'discrete'], ['recursive', 'discrete'], ['separable'], ['stable'], ['stable'], ['two-dimensional', 'discrete'], ['varying'], ['Filter', 'bank'], ['Filter', 'bank'], ['Filter', 'bank'], ['perfect', 'reconstruction'], ['separable'], ['separable'], ['Finite', 'elements'], ['Finite', 'elements'], ['Finite', 'elements'], ['Fix-Strang', 'condition'], ['Fix-Strang', 'condition'], ['Fix-Strang', 'condition'], ['Folded', 'wavelet', 'basis'], ['lifting'], ['Fourier', 'integral'], ['amplitude', 'decay'], ['convolution', 'theorem'], ['in', 'L2(R)'], ['in', 'L1(R)'], ['inverse'], ['Parseval', 'formula'], ['Plancherel', 'formula'], ['properties'], ['rotation'], ['sampling'], ['slice', 'theorem'], ['slice', 'theorem'], ['support'], ['two-dimensional'], ['uncertainty', 'principle'], ['Fourier', 'series'], ['Fourier', 'series'], ['approximation'], ['inversion'], ['Parseval', 'formula'], ['pointwise', 'convergence'], ['random', 'measurements'], ['dimension'], ['noise'], ['Fractional', 'Brownian'], ['Fractional', 'Brownian'], ['algorithm'], ['analysis'], ['de\xef\xac\x81nition'], ['de\xef\xac\x81nition'], ['dual'], ['dual'], ['dual', 'wavelet'], ['projector'], ['synthesis'], ['tight'], ['tight'], ['tight'], ['tight'], ['wavelet'], ['windowed', 'Fourier'], ['Frequency', 'modulation'], ['Frequency', 'ridges'], ['Frobenius', 'norm'], ['Fubini\xe2\x80\x99s', 'theorem'], ['Gabor'], ['dictionary'], ['wavelet'], ['wavelet'], ['function'], ['function'], ['function'], ['function'], ['matrix'], ['process'], ['process'], ['process'], ['process'], ['white', 'noise'], ['Geometry'], ['Gibbs', 'oscillations'], ['Gibbs', 'oscillations'], ['Gibbs', 'oscillations'], ['Gram', 'matrix'], ['Gram-Schmidt', 'orthogonalization'], ['Gray', 'code'], ['exponent'], ['norm'], ['space'], ['space'], ['Haar', 'wavelet'], ['Haar', 'wavelet'], ['Haar', 'wavelet'], ['Hard', 'thresholding'], ['Hausdorff', 'dimension'], ['Heat', 'diffusion'], ['box'], ['box'], ['box'], ['box'], ['box'], ['box'], ['uncertainty'], ['uncertainty'], ['uncertainty'], ['uncertainty'], ['uncertainty'], ['Hilbert', 'space'], ['Histogram'], ['Histogram'], ['Histogram'], ['Huffman', 'code'], ['Huffman', 'code'], ['Hurst', 'exponent'], ['Hyperrectangle'], ['Hyperrectangle'], ['Illusory', 'contours'], ['Impulse', 'response'], ['Impulse', 'response'], ['discrete'], ['discrete'], ['Incoherence'], ['Inpainting'], ['Instantaneous', 'frequency'], ['Instantaneous', 'frequency'], ['Instantaneous', 'frequency'], ['Interpolation'], ['Interpolation'], ['Interpolation'], ['Deslauriers-Dubuc'], ['Deslauriers-Dubuc'], ['function'], ['Lagrange'], ['spline'], ['wavelets'], ['Inverse', 'problem'], ['compressive', 'sensing'], ['super-resolution'], ['thresholding'], ['Iterative', 'thresholding'], ['Jackson', 'inequality'], ['Jensen', 'inequality'], ['JPEG'], ['JPEG'], ['JPEG-2000'], ['JPEG-2000'], ['approximation'], ['basis'], ['basis'], ['basis'], ['basis'], ['basis'], ['Kraft', 'inequality'], ['Kraft', 'inequality'], ['approximation'], ['approximation'], ['basis', 'pursuit'], ['basis', 'pursuit'], ['basis', 'pursuit'], ['fast', 'transform'], ['frequency', 'transform'], ['orthogonal', 'basis'], ['orthogonal', 'transform'], ['projector'], ['Lazy', 'wavelet'], ['Least', 'favorable', 'distribution'], ['Left', 'inverse'], ['Legendre', 'transform'], ['Level', 'set'], ['Level', 'set'], ['Level', 'set'], ['Level', 'set'], ['Level', 'set'], ['Lifting'], ['dual'], ['factorization'], ['prediction'], ['update'], ['Bayes', 'risk'], ['estimation'], ['estimation'], ['programming'], ['exponent'], ['exponent'], ['exponent'], ['Fourier', 'condition'], ['in', 'two', 'dimensions'], ['regularity'], ['wavelet', 'condition'], ['wavelet', 'condition'], ['wavelet', 'maxima'], ['Littlewood-Paley', 'sum'], ['basis'], ['basis'], ['basis'], ['basis'], ['discrete'], ['discrete'], ['quad-tree'], ['tree'], ['tree'], ['two-dimensional'], ['Local', 'stationarity'], ['Loss', 'function'], ['M-band', 'wavelets'], ['Mallat', 'algorithm'], ['Markov', 'chain'], ['Masking', 'noise'], ['Masking', 'noise'], ['Matching', 'pursuit'], ['Matching', 'pursuit'], ['Matching', 'pursuit'], ['denoising'], ['fast', 'calculation'], ['orthogonal'], ['wavelet', 'packets'], ['curves'], ['of', 'wavelet', 'transform'], ['of', 'wavelet', 'transform'], ['of', 'wavelet', 'transform'], ['propagation'], ['Median', '\xef\xac\x81lter'], ['Mesh'], ['Mesh'], ['Mexican', 'hat', 'wavelet'], ['Mexican', 'hat', 'wavelet'], ['wavelet'], ['wavelet', 'packets'], ['Minimax'], ['estimation'], ['estimation'], ['risk'], ['risk'], ['risk'], ['risk'], ['risk'], ['risk'], ['theorem'], ['Mirror', 'wavelet', 'basis'], ['Missing', 'data'], ['Model', 'selection'], ['Modulus', 'maxima'], ['Modulus', 'maxima'], ['Modulus', 'of', 'continuity'], ['Mother', 'wavelet'], ['Moyal', 'formula'], ['MP3'], ['MPEG'], ['MRI', 'imaging'], ['Multichannel', 'signals'], ['Multifractal'], ['Multifractal'], ['partition', 'function'], ['scaling', 'exponent'], ['de\xef\xac\x81nition'], ['piecewise', 'constant'], ['piecewise', 'constant'], ['piecewise', 'constant'], ['Shannon'], ['Shannon'], ['Shannon'], ['Shannon'], ['splines'], ['splines'], ['splines'], ['Multiscale', 'derivative'], ['Multiwavelets'], ['Multiwavelets'], ['MUSICAM'], ['Mutual', 'coherence'], ['Neural', 'network'], ['Norm'], ['L2(R)'], ['(cid:2)2(Z)'], ['(cid:2)p'], ['(cid:2)p'], ['(cid:2)p'], ['l1'], ['l', '0'], ['sup', 'for', 'operators'], ['weighted'], ['weighted'], ['NP-hard'], ['adjoint'], ['projector'], ['sup', 'norm'], ['time-invariant'], ['time-invariant'], ['attenuation'], ['attenuation'], ['estimation'], ['projection'], ['projection'], ['basis'], ['projector'], ['Orthosymmetric', 'set'], ['Orthosymmetric', 'set'], ['Parseval', 'formula'], ['Parseval', 'formula'], ['Partition', 'function'], ['Penalized', 'estimation'], ['constant'], ['constant'], ['constant'], ['polynomial'], ['in', '1D'], ['in', '1D'], ['in', '2D'], ['Pixel'], ['Plancherel', 'formula'], ['Plancherel', 'formula'], ['Poisson', 'formula'], ['Poisson', 'formula'], ['approximation'], ['Posterior', 'distribution'], ['Power', 'spectrum'], ['Power', 'spectrum'], ['Pre-echo'], ['Prediction'], ['Pre\xef\xac\x81x', 'code'], ['Principal', 'directions'], ['Principal', 'directions'], ['Prior', 'distribution'], ['Prior', 'set'], ['Pseudo', 'inverse'], ['PSNR'], ['basis'], ['matching'], ['matching'], ['orthogonal', 'matching'], ['Quad-tree'], ['Quad-tree'], ['Quad-tree'], ['convex', 'hull'], ['convex', 'hull'], ['convexity'], ['Quadrature', 'mirror', '\xef\xac\x81lters'], ['Quadrature', 'mirror', '\xef\xac\x81lters'], ['Quantization'], ['Quantization'], ['Quantization'], ['adaptive'], ['bin'], ['high', 'resolution'], ['high', 'resolution'], ['high', 'resolution'], ['low', 'resolution'], ['uniform'], ['vector'], ['weighted'], ['sampling'], ['wavelets'], ['Radon', 'transform'], ['Radon', 'transform'], ['Radon', 'transform'], ['Random', 'sensing'], ['Random', 'shift', 'process'], ['Random', 'shift', 'process'], ['Rate', 'distortion'], ['Real', 'wavelet', 'transform'], ['energy', 'conservation'], ['inverse'], ['Tikhonov'], ['Tikhonov'], ['total', 'variation'], ['frame'], ['wavelet'], ['windowed', 'Fourier'], ['Residue'], ['Residue'], ['Restoration'], ['Restricted', 'isometry', 'constant'], ['Richardson', 'iteration'], ['wavelet'], ['windowed', 'Fourier'], ['Riemann', 'function'], ['Riemann-Lebesgue', 'lemma'], ['Riesz', 'basis'], ['Riesz', 'basis'], ['Riesz', 'basis'], ['Riesz', 'basis'], ['Riesz', 'basis'], ['Rihaczek', 'distribution'], ['Risk'], ['Risk'], ['Run-length', 'code'], ['Block'], ['generalized', 'theorems'], ['generalized', 'theorems'], ['irregular'], ['redundant'], ['spline'], ['two-dimensional'], ['Whittaker'], ['Whittaker', 'theorem'], ['Whittaker', 'theorem'], ['Sampling', 'theorems'], ['Satellite', 'image'], ['Scaling', 'equation'], ['Scaling', 'equation'], ['Scaling', 'function'], ['Scaling', 'function'], ['Scaling', 'images'], ['Scalogram'], ['Segmentation'], ['Seismic', 'imaging'], ['function'], ['function'], ['set'], ['basis'], ['basis'], ['block', 'basis'], ['convolution'], ['decomposition'], ['\xef\xac\x81lter'], ['\xef\xac\x81lter', 'bank'], ['local', 'cosine', 'basis'], ['multiresolution'], ['wavelet', 'basis'], ['wavelet', 'basis'], ['wavelet', 'packet', 'basis'], ['code'], ['entropy', 'theorem'], ['multiresolution'], ['sampling', 'theorem'], ['Sigma-Delta'], ['Signal', 'to', 'Noise', 'Ratio'], ['Signi\xef\xac\x81cance', 'map'], ['Signi\xef\xac\x81cance', 'map'], ['Signi\xef\xac\x81cance', 'map'], ['Signi\xef\xac\x81cance', 'map'], ['Singular', 'value', 'decomposition'], ['Singular', 'value', 'decomposition'], ['Singular', 'values'], ['Singular', 'values'], ['Singularity'], ['Singularity'], ['spectrum'], ['SNR'], ['differentiability'], ['differentiability'], ['space'], ['space'], ['space'], ['Soft', 'thresholding'], ['Sonar'], ['model'], ['model'], ['separation'], ['Source', 'separation'], ['Source', 'separation'], ['Source', 'separation'], ['Sparse', 'spike', 'deconvolution'], ['Sparse', 'spike', 'deconvolution'], ['Spectrogram'], ['of', 'singularity'], ['operator'], ['power'], ['Speech'], ['Speech'], ['approximation'], ['multiresolution'], ['sampling'], ['wavelet', 'basis'], ['Stationary', 'process'], ['circular'], ['locally'], ['Stein', 'Estimator'], ['Super-resolution'], ['Super-resolution'], ['Super-resolution'], ['approximation'], ['recovery'], ['Sure', 'threshold'], ['Sure', 'threshold'], ['Symmetric', '\xef\xac\x81lters'], ['Symmetric', 'operator'], ['Symmlets'], ['Symmlets'], ['Tensor', 'product'], ['Tensor', 'product'], ['Texture', 'discrimination'], ['block'], ['estimation'], ['estimation'], ['estimation'], ['hard'], ['hard'], ['hard'], ['inverse', 'problem'], ['iterative'], ['risk'], ['risk'], ['soft'], ['soft'], ['Sure'], ['Sure'], ['threshold', 'choice'], ['threshold', 'choice'], ['translation', 'invariant'], ['translation', 'invariant'], ['wavelets'], ['wavelets'], ['Tikhonov', 'regularization'], ['Tikhonov', 'regularization'], ['atom'], ['atom'], ['plane'], ['plane'], ['resolution'], ['resolution'], ['resolution'], ['resolution'], ['resolution'], ['resolution'], ['140'], ['140'], ['Tomography'], ['Tomography'], ['Tomography'], ['backprojection'], ['Tonality'], ['Total', 'variation'], ['Total', 'variation'], ['Total', 'variation'], ['Wavelet', 'basis'], ['Wavelet', 'basis'], ['discrete', 'signal'], ['function'], ['image'], ['Transfer', 'function'], ['analog'], ['discrete'], ['Transform', 'code'], ['Transform', 'code'], ['Transform', 'code'], ['JPEG'], ['JPEG'], ['with', 'wavelets'], ['with', 'wavelets'], ['Transient'], ['Translation', 'invariance'], ['Translation', 'invariance'], ['Translation', 'invariance'], ['Translation', 'invariance'], ['561'], ['561'], ['561'], ['Transposition'], ['Transposition'], ['Transposition'], ['Triangulation'], ['Triangulation'], ['Delaunay'], ['Turbulence'], ['Uncertainty', 'principle'], ['Uncertainty', 'principle'], ['Uncertainty', 'principle'], ['Uncertainty', 'principle'], ['Uncertainty', 'principle'], ['Uniform', 'sampling'], ['Vanishing', 'moments'], ['Vanishing', 'moments'], ['Vanishing', 'moments'], ['Vanishing', 'moments'], ['Vanishing', 'moments'], ['352'], ['352'], ['352'], ['352'], ['Variance', 'estimation'], ['Video', 'compression'], ['Video', 'compression'], ['Vision'], ['Von', 'Koch', 'fractal'], ['Walsh', 'wavelet', 'packets'], ['directional'], ['seismic'], ['Battle-Lemari\xc3\xa9'], ['Battle-Lemari\xc3\xa9'], ['boundary'], ['boundary'], ['choice'], ['choice'], ['Coi\xef\xac\x82ets'], ['Daubechies'], ['Daubechies'], ['discrete'], ['folded'], ['graphs'], ['Haar'], ['interval'], ['interval'], ['interval'], ['lazy'], ['lifting'], ['M-band'], ['M-band'], ['Meyer'], ['mirror'], ['non-separable'], ['on', 'surfaces'], ['orthogonal'], ['periodic'], ['quincunx'], ['regularity'], ['separable'], ['Shannon'], ['spherical'], ['Symmlets'], ['Wavelet', 'packet', 'basis'], ['Wavelet', 'packet', 'basis'], ['Wavelet', 'packet', 'basis'], ['Wavelet', 'packet', 'basis'], ['626'], ['quad-tree'], ['tree'], ['two-dimensional'], ['Walsh'], ['Wavelet', 'transform'], ['admissibility'], ['admissibility'], ['analytic'], ['continuous'], ['continuous'], ['decay'], ['decay'], ['dyadic'], ['frame'], ['lifting'], ['maxima'], ['maxima'], ['multiscale', 'differentiation'], ['real'], ['ridges'], ['ridges'], ['Weak', 'convergence'], ['White', 'noise'], ['White', 'noise'], ['Wiener', 'estimator'], ['Wiener', 'estimator'], ['Wiener', 'estimator'], ['Wiener', 'estimator'], ['cross', 'terms'], ['discrete'], ['distribution'], ['distribution'], ['distribution'], ['distribution'], ['instantaneous', 'frequency'], ['interferences'], ['marginals'], ['positivity'], ['Blackman'], ['design'], ['design'], ['design'], ['discrete'], ['Gaussian'], ['Hamming'], ['Hanning'], ['Hanning'], ['rectangle'], ['scaling'], ['side-lobes'], ['side-lobes'], ['side-lobes'], ['Windowed', 'Fourier', 'transform'], ['Windowed', 'Fourier', 'transform'], ['discrete'], ['energy', 'conservation'], ['frame'], ['inverse'], ['reproducing', 'kernel'], ['ridges'], ['Zak', 'transform'], ['Zero-tree'], ['Zygmund', 'class']]
l2 = [' 620', ' 457', ' 466', ' 563', ' 758', ' 156', ' 381', ' 427', ' 431', ' 624', ' 147', ' 176', ' 240', ' 61', ' 69', ' 81', ' 303', ' 98', ' 146', ' 57', ' 117', ' 7', ' 65', '', ' 742', ' 88', ' 108', ' 108', ' 116', ' 109', ' 129', ' 457', ' 463', ' 468', ' 464', ' 442', ' 455', ' 8', ' 436', ' 442', ' 468', ' 551', ' 9', ' 451', ' 512', ' 551', ' 9', ' 23', ' 455', ' 615', ' 9', ' 442', ' 491', ' 494', '', ' 527', ' 15', ' 89', ' 92', ' 102', ' 109', ' 92', ' 502', ' 117', ' 124', ' 132', ' 118', ' 125', ' 132', ' 163', ' 672', ' 644', ' 55', ' 185', ' 410', ' 754', ' 631', ' 161', ' 306', ' 309', ' 757', ' 757', ' 660', ' 161', ' 265', ' 757', ' 25', ' 25', ' 664', ' 665', ' 684', ' 663', ' 281', ' 291', '', ' 12', ' 536', ' 545', ' 12', ' 536', ' 545', ' 732', ' 454', ' 460', ' 455', ' 459', ' 514', ' 612', ' 393', ' 431', ' 504', ' 662', ' 622', ' 623', ' 629', ' 623', ' 626', ' 174', ' 293', ' 624', ' 310', ' 311', ' 350', ' 312', ' 312', ' 314', ' 369', ' 311', ' 312', ' 369', ' 345', ' 311', ' 744', ' 401', ' 519', ' 404', ' 407', ' 401', ' 402', ' 576', ' 577', ' 442', ' 444', ' 317', ' 322', ' 369', ' 47', ' 46', ' 440', ' 446', ' 460', ' 461', '', ' 711', ' 50', ' 467', ' 514', ' 603', ' 712', ' 70', ' 174', ' 266', ' 56', ' 230', ' 245', ' 242', ' 251', ' 243', ' 623', ' 570', ' 755', ' 675', ' 744', ' 129', ' 134', ' 94', ' 126', ' 133', ' 94', ' 148', ' 50', ' 340', ' 492', ' 507', ' 491', ' 490', ' 527', ' 516', ' 527', ' 488', ' 485', ' 488', ' 485', ' 506', ' 500', ' 145', ' 150', ' 146', ' 658', ' 656', ' 296', ' 478', ' 689', ' 692', ' 286', ' 292', ' 311', ' 482', ' 614', ' 482', ' 506', ' 482', ' 483', ' 654', ' 29', ' 728', ' 754', ' 618', ' 537', ' 215', ' 457', ' 165', ' 4', '', ' 306', ' 284', ' 505', ' 292', ' 298', ' 298', ' 754', ' 587', ' 592', ' 754', ' 587', ' 76', ' 83', ' 301', ' 320', ' 394', '', ' 541', ' 34', ' 71', ' 79', ' 80', ' 34', ' 83', ' 77', ' 74', ' 37', ' 403', ' 418', ' 519', ' 406', ' 425', ' 404', ' 418', ' 407', ' 422', ' 642', ' 447', ' 762', ' 447', ' 539', ' 762', ' 270', ' 277', ' 194', ' 476', ' 570', ' 197', ' 292', ' 406', ' 409', ' 407', ' 408', ' 99', ' 541', ' 724', ' 246', ' 612', ' 616', ' 650', ' 646', ' 663', ' 621', ' 646', ' 663', ' 33', ' 40', ' 94', ' 719', ' 763', ' 41', ' 60', ' 764', ' 76', ' 540', '', ' 77', ' 77', ' 83', ' 308', ' 563', ' 11', ' 484', ' 517', ' 520', ' 504', ' 274', ' 753', ' 22', ' 159', ' 22', ' 162', ' 170', ' 190', '', ' 224', ' 174', ' 189', ' 232', ' 471', ' 230', ' 236', ' 235', ' 236', ' 230', ' 37', ' 71', ' 76', ' 516', ' 527', ' 77', ' 101', ' 39', ' 73', ' 643', ' 155', ' 105', ' 111', ' 96', ' 486', ' 495', ' 744', ' 12', ' 544', ' 578', ' 236', ' 565', ' 550', ' 551', ' 590', ' 705', ' 550', ' 553', ' 539', ' 25', ' 679', ' 78', ' 85', ' 310', ' 114', ' 175', ' 301', ' 349', ' 298', ' 346', ' 753', ' 34', ' 37', ' 34', ' 71', ' 71', ' 337', ' 40', ' 74', ' 74', ' 87', ' 83', ' 34', ' 71', ' 82', ' 351', ' 4', ' 176', ' 298', ' 304', ' 346', ' 399', ' 361', ' 442', ' 471', ' 286', ' 330', '', ' 320', ' 369', ' 2', ' 42', ' 37', ' 38', ' 35', ' 36', ' 39', ' 39', ' 38', ' 53', ' 60', ' 54', ' 726', ' 45', ' 51', ' 44', ' 72', ' 438', ' 438', ' 73', ' 73', ' 73', ' 733', ' 243', ' 258', ' 254', ' 261', ' 164', ' 155', ' 22', ' 156', ' 160', ' 187', ' 180', ' 166', ' 156', ' 156', ' 183', ' 197', ' 476', ' 178', ' 182', ' 117', ' 17', ' 688', ' 754', ' 14', ' 650', ' 111', ' 190', ' 41', ' 45', ' 126', ' 137', ' 731', ' 484', ' 499', ' 501', ' 540', ' 548', ' 510', ' 47', ' 69', ' 440', ' 157', ' 648', ' 386', ' 206', ' 464', ' 445', ' 464', ' 2', ' 3', ' 291', ' 668', ' 243', ' 221', ' 16', ' 90', ' 109', ' 388', ' 420', ' 628', ' 15', ' 43', ' 89', ' 90', ' 98', ' 755', ' 491', ' 506', ' 509', ' 488', ' 494', ' 254', ' 587', ' 590', ' 236', ' 34', ' 82', ' 70', ' 82', ' 730', ' 722', ' 94', ' 115', ' 138', ' 61', ' 472', ' 725', ' 332', ' 337', ' 328', ' 337', ' 331', ' 335', ' 700', ' 728', ' 713', ' 27', ' 668', ' 454', ' 754', ' 11', ' 519', ' 11', ' 523', ' 447', ' 447', ' 450', ' 499', ' 539', ' 762', ' 486', ' 507', ' 612', ' 665', ' 664', ' 665', ' 684', ' 424', ' 418', ' 416', ' 410', ' 411', ' 352', ' 547', ' 159', ' 248', ' 50', ' 232', ' 467', ' 471', ' 728', ' 350', ' 355', ' 367', ' 353', ' 355', ' 543', ' 12', ' 537', ' 662', ' 205', ' 456', ' 460', ' 206', ' 230', ' 206', ' 211', ' 212', ' 219', ' 212', ' 20', ' 418', ' 440', ' 501', ' 423', ' 429', ' 430', ' 426', ' 429', ' 630', ' 501', ' 536', ' 390', ' 298', ' 532', ' 561', ' 570', ' 24', ' 642', ' 679', ' 656', ' 645', ' 648', ' 646', ' 232', ' 218', ' 231', ' 245', ' 221', ' 565', ' 361', ' 472', ' 103', ' 180', ' 289', ' 418', ' 7', ' 12', ' 544', ' 12', ' 544', ' 545', ' 586', ' 590', ' 606', ' 545', ' 711', ' 722', ' 617', ' 218', ' 230', ' 334', ' 92', ' 139', ' 503', ' 483', ' 743', ' 688', ' 19', ' 242', ' 248', ' 248', ' 264', ' 265', ' 277', ' 339', ' 265', ' 266', ' 277', ' 339', ' 266', ' 277', ' 340', ' 208', ' 287', ' 373', ' 502', ' 678', ' 645', ' 754', ' 756', ' 756', ' 454', ' 460', ' 755', ' 660', ' 665', ' 758', ' 498', ' 520', ' 613', ' 758', ' 759', ' 758', ' 33', ' 70', ' 550', ' 590', ' 549', ' 551', ' 557', ' 757', ' 759', ' 592', ' 606', ' 39', ' 757', ' 248', ' 617', ' 265', ' 277', ' 339', ' 543', ' 456', ' 599', ' 471', ' 80', ' 39', ' 757', ' 41', ' 285', ' 330', ' 536', ' 541', ' 763', ' 502', ' 606', ' 485', ' 449', ' 762', ' 536', ' 544', ' 159', ' 508', ' 660', ' 642', ' 679', ' 648', ' 396', ' 430', ' 624', ' 587', ' 592', ' 587', ' 302', ' 371', ' 11', ' 483', ' 493', ' 502', ' 493', ' 493', ' 496', ' 507', ' 510', ' 494', ' 484', ' 526', ' 359', ' 359', ' 53', ' 726', ' 743', ' 731', ' 449', ' 542', ' 529', ' 103', ' 105', ' 105', ' 700', ' 722', ' 728', ' 167', ' 106', ' 97', ' 643', ' 648', ' 700', ' 730', ' 163', ' 129', ' 122', ' 260', ' 56', ' 22', ' 65', ' 161', ' 265', ' 757', ' 147', ' 12', ' 536', ' 519', ' 69', ' 69', ' 328', ' 158', ' 168', ' 70', ' 81', ' 68', ' 61', ' 81', ' 7', ' 712', ' 270', ' 330', ' 106', ' 267', ' 724', ' 109', ' 192', ' 719', ' 19', ' 244', ' 242', ' 84', ' 760', ' 402', ' 83', ' 84', ' 83', ' 399', ' 431', ' 338', ' 338', ' 341', ' 399', ' 488', ' 486', ' 266', ' 61', ' 168', ' 541', ' 510', ' 516', ' 519', ' 526', ' 27', ' 701', ' 156', ' 759', ' 19', ' 205', ' 246', ' 541', ' 438', ' 443', ' 439', ' 443', ' 459', ' 553', ' 126', ' 117', ' 744', ' 744', ' 29', ' 687', ' 744', ' 719', ' 733', ' 92', ' 246', ' 759', ' 763', ' 117', ' 482', ' 457', ' 266', ' 70', ' 281', ' 450', ' 540', ' 501', ' 559', ' 28', ' 713', ' 724', ' 23', ' 25', ' 558', ' 566', ' 313', ' 758', ' 294', ' 565', ' 339', ' 760', ' 191', ' 576', ' 14', ' 568', ' 705', ' 552', ' 565', ' 668', ' 27', ' 668', ' 552', ' 592', ' 553', ' 565', ' 558', ' 566', ' 556', ' 705', ' 561', ' 566', ' 566', ' 606', ' 701', ' 723', ' 15', ' 89', ' 15', ' 90', ' 90', ' 98', ' 109', ' 124', ' 135', '', ' 146', ' 388', ' 53', ' 726', ' 743', ' 55', ' 502', ' 440', ' 461', ' 728', ' 278', ' 281', ' 47', ' 46', ' 50', ' 83', ' 37', ' 71', ' 11', ' 482', ' 483', ' 11', ' 519', ' 11', ' 514', ' 628', ' 168', ' 226', ' 422', '', ' 566', ' 589', ' 646', ' 118', ' 125', ' 132', ' 361', ' 472', ' 475', ' 258', ' 16', ' 43', ' 89', ' 90', ' 98', ' 60', ' 208', ' 284', ' 330', ' 342', '', ' 358', ' 443', ' 455', ' 524', ' 565', ' 483', ' 654', ' 189', ' 244', ' 387', ' 189', ' 719', ' 291', ' 457', ' 301', ' 322', ' 284', ' 524', ' 296', ' 3', ' 292', ' 306', ' 320', ' 302', ' 291', ' 317', ' 369', ' 442', ' 352', ' 350', ' 390', ' 504', ' 289', ' 711', ' 359', ' 361', ' 3', ' 318', ' 359', ' 287', ' 341', ' 289', ' 365', ' 294', ' 19', ' 382', ' 504', '', ' 710', ' 430', ' 379', ' 395', ' 387', ' 17', ' 106', ' 179', ' 109', ' 17', ' 102', ' 211', ' 212', ' 170', ' 178', ' 356', ' 218', ' 232', ' 208', ' 103', ' 129', ' 216', ' 763', ' 540', ' 548', ' 538', ' 539', ' 542', ' 589', ' 140', ' 149', ' 89', ' 136', ' 140', ' 651', ' 138', ' 140', ' 139', ' 143', ' 99', ' 75', ' 99', ' 419', ' 75', ' 99', ' 99', ' 75', ' 99', ' 75', ' 98', ' 75', ' 99', ' 125', ' 16', ' 92', ' 101', ' 96', ' 182', ' 96', ' 97', ' 122', ' 203', ' 526', ' 212']

print len(l1)
print len(l2)
for faf in range(len(l2)):
    tex = l1[faf]
    tex2 = l2[faf]
    if any(c.isalpha() for c in tex2) or len(tex2)>4 or tex2=='':
        continue
    print tex
    m = convert('IP5.pdf', pages=[int(tex2)+18])

    m = m.split('\n\n')
    f2 = open("xxIP5.txt",'a')
    f3 = open("yyIP5.txt",'a')
    for k in m:
        if len(k)>150:
            s = ""
            k = list(k)
            chick = []
            mac = 0
            while mac<len(k):
            #print k[mac]
                if k[mac]=='\n':
                #k[m] = " "
                    chick.append(' ')

                elif k[mac]=='-':
                    temp = mac+1
                #print "True"
                    if temp!=len(k) and k[temp]=='\n':
                    #print "True"
                        mac = mac+1
                    else:
                        chick.append(k[mac].lower())
                else:
                    chick.append(k[mac].lower())
                mac = mac+1
            k = chick

            
        
            print "".join(k).strip()
            temp = "".join(k)

            temp.strip()
            f2.write(temp)
            f2.write("\n")

            temp = temp.split(' ')
            l = []
            for cha in temp:
                #if "isymmetric" in cha: #or "pproxmia" in cha:
                #    l.append(1)
                check = 0
                for vv in tex:
                    if vv.lower() in cha and vv!='':
                        print cha
                        l.append(1)
                        check=1
                        break
                if check==0:
                    l.append(0)
            print len(temp)
            print len(l)
            lll = ",".join(str(x) for x in l)
            f3.write(lll)
            f3.write("\n")
            print "\n"
            print l
            print "\n"
    f2.close()
    f3.close()