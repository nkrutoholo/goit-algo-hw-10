import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi


def f(x):
    return x ** 2


a = 0
b = 2


def monte_carlo_integration(func, a, b, n=1_000_000):
    x_random = np.random.uniform(a, b, n)
    mean_height = np.mean(func(x_random))
    return (b - a) * mean_height


def plot_function():
    x = np.linspace(-0.5, 2.5, 400)
    y = f(x)

    fig, ax = plt.subplots()
    ax.plot(x, y, "r", linewidth=2)

    ix = np.linspace(a, b)
    iy = f(ix)
    ax.fill_between(ix, iy, color="gray", alpha=0.3)

    ax.set_xlim([x[0], x[-1]])
    ax.set_ylim([0, max(y) + 0.1])
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.axvline(x=a, color="gray", linestyle="--")
    ax.axvline(x=b, color="gray", linestyle="--")
    ax.set_title(f"Графік інтегрування f(x) = x^2 від {a} до {b}")
    plt.grid()
    plt.savefig("integration_plot.png", dpi=100)
    print("Графік збережено у integration_plot.png")
    plt.show()


def main():
    mc_result = monte_carlo_integration(f, a, b)
    print(f"Monte Carlo result:  {mc_result:.6f}")

    quad_result, quad_error = spi.quad(f, a, b)
    print(f"SciPy quad result:   {quad_result:.6f}  (error {quad_error:.2e})")

    analytic = (b ** 3 - a ** 3) / 3
    print(f"Analytic value:      {analytic:.6f}")

    diff = abs(mc_result - quad_result)
    print(f"Difference (MC - quad): {diff:.6f}")

    plot_function()


if __name__ == "__main__":
    main()
