import numpy as np
import matplotlib.pyplot as plt

# Given data
x = np.array([5, 10, 15, 20, 25, 30, 35, 40])
y = np.array([40, 30, 25, 40, 18, 20, 22, 15])

# Lagrange Interpolation
def lagrange_interpolation(x, y, xi):
    def basis(i, xi):
        p = [(xi - x[j]) / (x[i] - x[j]) for j in range(len(x)) if j != i]
        return np.prod(p)
    yi = sum(y[i] * basis(i, xi) for i in range(len(x)))
    return yi

# Newton Interpolation
def newton_interpolation(x, y, xi):
    n = len(x)
    divided_diff = np.zeros((n, n))
    divided_diff[:,0] = y
    for j in range(1, n):
        for i in range(n - j):
            divided_diff[i, j] = (divided_diff[i + 1, j - 1] - divided_diff[i, j - 1]) / (x[i + j] - x[i])
    def newton_basis(xi, k):
        product = 1.0
        for j in range(k):
            product *= (xi - x[j])
        return product
    yi = divided_diff[0, 0]
    for k in range(1, n):
        yi += divided_diff[0, k] * newton_basis(xi, k)
    return yi

# Function to choose interpolation method and plot results
def plot_interpolation(method):
    xi = np.linspace(5, 40, 500)
    if method == 'lagrange':
        yi = [lagrange_interpolation(x, y, i) for i in xi]
        label = 'Lagrange Interpolation'
        line_style = '-'
    elif method == 'newton':
        yi = [newton_interpolation(x, y, i) for i in xi]
        label = 'Newton Interpolation'
        line_style = '--'
    else:
        raise ValueError("Invalid method. Choose 'lagrange' or 'newton'.")
    
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, 'o', label='Data points')
    plt.plot(xi, yi, line_style, label=label)
    plt.xlabel('Tegangan, x (kg/mm²)')
    plt.ylabel('Waktu patah, y (jam)')
    plt.title('Interpolasi Polinom {}'.format(label))
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    import sys
    method = sys.argv[1]
    plot_interpolation(method)
