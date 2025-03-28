> 假设$f$关于$u$满足Lipschitz条件，$k$步法相容，不妨设为$p$阶方法，可以将整体误差的表达式改写成$$\sum_{j=0}^k\alpha_je_{n+j}=\tau b_n^*,\quad b_n^* =b_n+c_{p+1}\tau^pu^{(p+1)}(t_n)+O(\tau^{p+1}) $$，有误差估计式$$\Vert E_n\Vert \leq e^{K_2T}((K_1+K_2\tau))\Vert E_0\Vert+M_{p+1}T\tau^p $$，其中，$E_0$是初始误差向量，$M_{p+1}=c_{p+1}|\alpha^{-1}|\sup_t |u^{(p+1)}(t) |+1  $

证明：

令$$E_n=\begin{pmatrix}
  {e}_{n+k-1}, \dots, {e}_n
\end{pmatrix}^T$$

令$$C=\begin{pmatrix}
      -a_k^{-1}a_{k-1} & -a_k^{-1}a_{k-1} & \dots & -a_k^{-1}a_1, & -a_k^{-1}a_0\\
  1 & & & & 0 \\
   & 1 & & & 0\\
   & & \ddots & & 0\\
   & & & 1 & 0
\end{pmatrix} $$，$$B_n=\begin{pmatrix}
  a_k^{-1}\tau b^*,0,\dots,0
\end{pmatrix}^T $$

那么就有$$E_{n+1}=CE_n+B_n $$，进而就有$$E_n=C^nE_0+\sum_{l=0}^{n-1}C^lB_{n-l-1} $$

就有$$\Vert E_n\Vert\leq \Vert C\Vert^n\Vert E_0\Vert+a_k^{-1}\tau b^* $$

应用Gronwell不等式，有$$\Vert E_n\Vert\leq e^{a_k^{-1}b^*T}(\Vert C\Vert^n\Vert E_0\Vert+M_{p+1}T\tau^p) $$

> 证明线性多步法$$u_{n+2}+(b-1)u_{n+1}-bu_n=\frac{1}{4}\tau[(b+3)f_{n+2}+(3b+1)f_n] $$当$b\neq -1$时阶是$2$，当$b=-1$时阶是$3$。又$b=-1$是不稳定的，将$b=-1$的方法用到$$u'=u,\quad u(0)=1$$，解出相应的差分方程($u_0=1,u_1=1$)，说明方法发散

证明：

方法具有$p$阶的等价表述为，对数列$$c_p=\frac{1}{p!}\sum_{i=0}^{k}i^p\alpha_i-\frac{1}{(p-1)!}\sum_{i=0}^{k}i^{p-1}\beta_i $$，满足$$c_0=c_1=\dots=c_p=0,\quad c_{p+1}\neq 0 $$

在这里，$$\begin{equation}
    \nonumber
    \begin{split}
        c_0&=0\\
        c_1&=0\\
        c_2&=0\\
        c_3&=\frac{b+7}{6}-\frac{b+3}{2}\\
        c_4&=-\frac{7b+9}{24}
    \end{split}
\end{equation}$$

当$b\neq -1,\quad c_0=c_1=\dots=c_2=0,\quad c_{3}\neq 0$，此时为二阶。
当$b= -1,\quad c_0=c_1=\dots=c_3=0,\quad c_{4}\neq 0$，此时为三阶。

$b=-1$时，应用得到的差分方程为$$2u_{n+2}-4u_{n+1}+2u_n=\tau (u_{n+2}-u_n),\quad u_0=1,u_1=1 $$

将$u_0,u_1$条件代入，发现解为$u_2=1$，由此可得$u\equiv1$，与$\tau$的取值无关。

方程的解析解为$u(t)=e^t $。

可以发现方法确实发散。

> 定义$\alpha$的变化域，使线性多步法$$u_{n+3}+\alpha(u_{n+2}-u_{n+1})-u_n=\frac{1}{2}(3+\alpha)\tau(f_{n+2}+f_{n+1}) $$是稳定的，并说明方法的阶不能大于$2$。

k 步法稳定的充要条件是 \(\rho(\lambda)\) 的所有根均满足
\[
|\lambda|\le 1,
\]
且当 \(|\lambda|=1\)时，\(\lambda\)必须为单根。

在本题中，$\rho(\lambda)=\lambda^3+\alpha \lambda^2-\alpha\lambda-1=(\lambda-1)(\lambda^2+(\alpha-1)\lambda+1) $，其根有$\lambda=1,\frac{1-\alpha\pm\sqrt{\alpha^2-2\alpha-3}}{2} $，要使其均满足$|\lambda|\leq 1$，且$1$为单根，要求$$ |\frac{1-\alpha\pm\sqrt{\alpha^2-2\alpha-3}}{2}|<1 $$，得到$\alpha\in(-1,3)$

> 证明方法$$u_{n+1}-u_n=\tau f_{n+1} $$对所有$\bar{\tau}\in(-\infty,0) $绝对稳定

绝对稳定的充要条件是稳定方程$$u_{n+1}-u_n=\bar{\tau} u_{n+1} $$的特征值均在单位圆内。其特征方程为$$(1-\bar{\tau})\lambda-1=0 $$，解为$$\lambda=\frac{1}{1-\bar{\tau}} $$，当$\bar{\tau}<0$时，总有$0<\lambda<1$，因此绝对稳定。

> 求二级二阶隐式Runge-Kutta方法$$u_{n+1}=u_n+\frac{1}{2}\tau(k_1+k_2) $$$$k_1=f(t_n,u_n),\quad k_2=f(t_{n+1},u_n+\frac{1}{2}\tau(k_1+k_2)) $$的绝对稳定域

绝对稳定域，一般的方法是$$\bar{\tau}=\frac{\rho(\lambda)}{\sigma(\lambda)} $$由$|\lambda|<1$在$\bar{\tau}$上对应的区域。

但是这里需要针对解出$k_1,k_2$

$$k_1=\mu u_n$$

$$k_2=\mu (u_n + \frac{1}{2}\tau\mu k_1+\frac{\tau}{2}k_2)$$

解得$k_2=\frac{\mu(u_n+\frac{1}{2}\bar{\tau}\mu u_n)}{1-\frac{\bar{\tau}}{2}}$

然后直接得到特征多项式$$\lambda-1-\bar{\tau}-\frac{1}{4}\bar{\tau}^2+\frac{1}{4}\bar{\tau}\lambda=0 $$

解出来，令$|\lambda|<1$，就有$|\frac{\bar{\tau}^2+4\bar{\tau}+4}{\bar{\tau}+4}|<1$解得$\bar{\tau}\in(-3,0) $


