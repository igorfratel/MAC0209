import matplotlib.pyplot as plt

#metodo analitico    
def analytical_method(a, b, N, alpha, beta, const):
    states_time = []
    states_position = []
    states_velocity = []
    delta = (b - a)/N
    t = 0
    y = alpha
    v = beta
    states_time.append(t)
    states_position.append(y)
    states_velocity.append(v)
    for i in range(1, N + 1):
        t = t + delta
        states_time.append(t)
        states_position.append(y + v*t + const*t*t/2)
        states_velocity.append(v + const*t)
    return states_time, states_position, states_velocity
    
#metodo numerico    
def euler_method(a, b, N, alpha, beta, const):
    states_time = []
    states_position = []
    states_velocity = []
    delta = (b - a)/N
    t = 0
    y = alpha
    v = beta
    states_time.append(t)
    states_position.append(y)
    states_velocity.append(v)
    for i in range(1, N + 1):
        y = y + v*delta
        v = v + const*delta
        states_time.append(t)
        states_position.append(y)
        states_velocity.append(v)
        t = t + delta
    return states_time, states_position, states_velocity
    
    
def main():
    euler_time,euler_position, euler_velocity = euler_method(0, 50, 100, 10, 0, -10)
    analytical_time, analytical_position, analytical_velocity = analytical_method(0, 50, 100, 10, 0, -10)
    plt.plot(analytical_time, analytical_position, color = 'g')
    plt.plot(analytical_time, analytical_velocity, color = 'b')
    plt.plot(euler_time, analytical_position, color = 'r')
    plt.plot(euler_time, analytical_velocity, color = 'c')
    plt.show()
main()
#MODIFICAR O PROGRAMA EM DOIS GRAFICOS E FAZER ELE PARAR QUANDO O OBJETO CHEGAR NO ZERO!!!!!!!!!
