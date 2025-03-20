import numpy as np
import matplotlib.pyplot as plt

def f(t, u):
    return u - t**2

def exact_solution(t):
    return (t**2 + 2 * t + 2) - 2 * np.exp(t)

def euler_method(f, t0, u0, T, tau):
    t_values = np.arange(t0, T + tau, tau)
    u_values = np.zeros_like(t_values)
    u_values[0] = u0
    
    for i in range(1, len(t_values)):
        u_values[i] = u_values[i-1] + tau * f(t_values[i-1], u_values[i-1])
    
    return t_values, u_values

def adams_bashforth_2(f, t0, u0, T, tau):
    t_values = np.arange(t0, T + tau, tau)
    u_values = np.zeros_like(t_values)
    
    # 使用Euler方法初始化
    u_values[0] = u0
    u_values[1] = u_values[0] + tau * f(t_values[0], u_values[0])
    
    for i in range(1, len(t_values) - 1):
        u_values[i+1] = u_values[i] + (tau / 2) * (3 * f(t_values[i], u_values[i]) - f(t_values[i-1], u_values[i-1]))
    
    return t_values, u_values

def adams_moulton_2(f, t0, u0, T, tau):
    t_values = np.arange(t0, T + tau, tau)
    u_values = np.zeros_like(t_values)
    
    # 使用Euler方法初始化
    u_values[0] = u0
    u_values[1] = u_values[0] + tau * f(t_values[0], u_values[0])
    
    for i in range(1, len(t_values) - 1):
        u_pred = u_values[i] + tau * f(t_values[i], u_values[i])
        u_values[i+1] = u_values[i] + (tau / 2) * (f(t_values[i], u_values[i]) + f(t_values[i+1], u_pred))
    
    return t_values, u_values

def milne_method(f, t0, u0, T, tau):
    t_values = np.arange(t0, T + tau, tau)
    u_values = np.zeros_like(t_values)
    
    # 使用Euler方法和Adams方法初始化前三步
    u_values[0] = u0
    u_values[1] = u_values[0] + tau * f(t_values[0], u_values[0])
    u_values[2] = u_values[1] + tau * f(t_values[1], u_values[1])
    
    for i in range(2, len(t_values) - 1):
        u_pred = u_values[i-3] + (4*tau/3) * (2*f(t_values[i-1], u_values[i-1]) - f(t_values[i-2], u_values[i-2]) + 2*f(t_values[i], u_values[i]))
        u_values[i+1] = (4*u_values[i] - u_values[i-2] + (4*tau/3) * f(t_values[i+1], u_pred)) / 3
    
    return t_values, u_values

def plot_results():
    t0, u0, T, tau = 0, 0, 1, 0.2
    t_exact = np.arange(t0, T + tau, tau)
    u_exact = exact_solution(t_exact)
    
    t_euler, u_euler = euler_method(f, t0, u0, T, tau)
    t_ab2, u_ab2 = adams_bashforth_2(f, t0, u0, T, tau)
    t_am2, u_am2 = adams_moulton_2(f, t0, u0, T, tau)
    t_milne, u_milne = milne_method(f, t0, u0, T, tau)
    
    plt.plot(t_exact, u_exact, 'k-', label='Exact Solution')
    plt.plot(t_euler, u_euler, 'bo-', label='Euler Method')
    plt.plot(t_ab2, u_ab2, 'r*-', label='Adams-Bashforth 2')
    plt.plot(t_am2, u_am2, 'g^-', label='Adams-Moulton 2')
    plt.plot(t_milne, u_milne, 'ms-', label='Milne Method')
    plt.xlabel('t')
    plt.ylabel('u(t)')
    plt.legend()
    plt.grid()
    plt.savefig('w4-1.png')
    plt.close()


    plt.plot(t_euler, abs(u_euler - u_exact), 'bo-', label='Euler Method')
    plt.plot(t_ab2, abs(u_ab2 - u_exact), 'r*-', label='Adams-Bashforth 2')
    plt.plot(t_am2, abs(u_am2 - u_exact), 'g^-', label='Adams-Moulton 2')
    plt.plot(t_milne, abs(u_milne - u_exact), 'ms-', label='Milne Method')
    plt.xlabel('t')
    plt.ylabel('u(t)')
    plt.legend()
    plt.grid()
    plt.savefig('w4-2.png')
    plt.close()

plot_results()
