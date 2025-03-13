![](w3-1.png)

证明：

先证误差不等式

$$u(t_n)=u(t_{n-1})+\tau F(t_{n-1},u(t_{n-1}),\tau)+\tau T_n $$
$$u_n=u_{n-1}+\tau F(t_{n-1},u_{n-1},\tau) $$

两式相减，有$$\begin{equation}
    \nonumber
    \begin{split}
        e_n &= e_{n-1}+\tau [F(t_{n-1},u(t_{n-1}),\tau)-F(t_{n-1},u_{n-1},\tau)]+\tau T_n\\
            & \leq e_{n-1}+\tau K e_{n-1}+\tau T_n\\
            & = (1+\tau K)^{n}e_0+\tau\sum_{i=0}^{n-1}(1+\tau K)^i T_{n-i}\\
            & \leq (1+\tau K)^ne_0+\frac{1}{K}[(1+\tau K)^n-1]A(\tau)\\
            & \leq e^{\tau nK}e_0+\frac{1}{K}[e^{\tau Kn}-1]A(\tau)\\
            & = e^{(T-t_0)K}e_0+\frac{e^{(T-t_0)K}-1}{K}A(\tau)
    \end{split}
\end{equation} $$


再证$u_n\to u(t_n)$


$$u(t_n)-u(t_{n-1})=\tau F(t_{n-1},u(t_{n-1}),\tau)+R_n(\tau) $$

因此就有$$\frac{1}{\tau}\int_{t_{n-1}}^{t_{n-1}+\tau}f(s,u(s))\text{d}s= F(t_{n-1},u(t_{n-1}),\tau)+T_n(\tau) $$

两边取极限，有$$\lim_{\tau\to 0}\frac{1}{\tau}\int_{t_{n-1}}^{t_{n-1}+\tau}f(s,u(s))\text{d}s= \lim_{\tau\to 0}F(t_{n-1},u(t_{n-1}),\tau)+ T_n(0)$$，即$$f(t_{n-1},u(t_{n-1}))=f(t_{n-1},u(t_{n-1}))+T_n(0) $$，因此$$T_n=0$$故$$e_n\leq  e^{(T-t_0)K}e_0$$，因此在$e_0=0$时有$e_n=0$

