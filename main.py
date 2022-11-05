import numpy as np
import matplotlib.pyplot as plot


def squ_sin(amp, f):
    # array of values between -2, 2
    n = np.linspace(-2, 2, 100)
    
    # sine wave
    sin = amp * np.sin(2* np.pi * f * n)
    
    # rectangular
    f1 = lambda t: (abs(t)<0.5).astype(float)

    # calc the convolution values 
    x = np.convolve(sin , f1(n))

    return x

def squ_cos(amp, f):
    # array of values between -2, 2
    n = np.linspace(-2, 2, 100)
    
    # array of cos discrete values 
    cos = amp * np.cos(2 * np.pi*f*n)

    # rectangular
    f1 = lambda t: (abs(t)<0.5).astype(float)
    
    # calc the convolution values
    x = np.convolve(cos , f1(n))

    return x
#   done/2

def trig_exp(f, T, t0):
    # t0 convolution at time ?
    # f => freq
    # T => period

    t = np.arange(-T, T, 1/f)

    
    f1 = lambda t: np.maximum(0, 1-abs(t))

    f2 = lambda t: (t>0) * np.exp(-2*t)
    
    # flipped function
    flipped = lambda tau: f2(t0 - tau)

    # convolution 
    product = lambda tau: f1(tau) * f2(t0 - tau)

    plot.plot(t, f1(t))
    plot.plot(t, flipped(t))
    plot.plot(t, product(t))
    return 
    #  done 

# exponential and sine
def exp_sin(f, T):
    t = np.arange(-T, T, 1/f)
    f1 = lambda t: (t>0) * np.exp(-2*t)
    f2 = lambda t: np.sin(2 * np.pi * t) * (t > 0)

    plot.plot(t, f1(t))
    plot.plot(t, f2(t))
    return 
    # done

plot.show()