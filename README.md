
# General description
Goverments act as Stackelberg leaders by trading energy, with the aim of minimizing their emissions, and eventually to maximize tax revenues. Within each country, energy producers act as Stackelberg followers and play a Nash game between themselves, aiming to maximize their profits given the regulations from Goverments.
Each country is interested to impose a tax that is not preventing profitable domestic production, as it is constrained to keep the domestic energy price less than a predetermined threshold. We present the optimization problems of the players formally below. For ease of understanding the quantities in {\color{rosso}red} are parameters, i.e., inputs to the model. And the quantities in {\color{blue}blue} are decision variables, decided by the country. Quantities in {\color{green}green} are variables of a {\em different} player influencing the country's problem.
Each country $$C$$ solves the following problem.
$$ \min \quad&:\quad  \left (
    \sum_{p\in \mathscr{P}} \Cemm\qi
     -\taxb \ti\qi
    \right)
    + \sum_{C'\in\mathscr{C}\setminus C}\piI[C']\qAimpI[C'\to C]
    - \piI[C]\qexp
$$

$$    \text{s.t.} \qquad & \ti \le \tiCap $$
$$    \qquad \qquad  \DemInt - \DemSlope \left( \sum_{p\in\mathscr{P}} \qi + \qimp - \qexp \right) \ge \piFloor $$
$$    \qquad \qquad  \sum_{C'\in\mathscr{C}}\qAimpI[C'\to C] = \qimp $$
$$    \qquad \qquad  \qi \in \sol (\text{Lower Level Nash Game})$$

$$\Cemm$$ is the emission penalty that $$p$$ encounters while producing a unit quantity of energy. This number is the product of cost incurred due to the emission of one unit of greenhouse gases ($GHG$), and the quantity of GHG emitted for each unit of energy produced by the producer $$p$$. $$\taxb$$ dictates whether objective should include the tax revenue earned by the government or not. $$\qi$$ is the quantity of energy produced by the producer $$p\in\mathscr{P}$, $$\qimp, \qexp$$ are respectively import and export quantities, and $$\DemInt, \DemSlope$$ are the intercept and the slope of the demand curve. The domestic price, for each country, is given by $$\DemInt - \DemSlope Q$$ where $$Q$$ is the domestic quantity of energy available. Finally, $$\piI[C']$$ is the price at which the country can import energy from other countries, hence the variable linking the optimization problems of different countries. Optionally for some countries, we introduce a  \emph{carbon tax} paradigm, where the tax imposed on the followers is proportional to the emissions they cause. i.e., there is a constraint $$\ti = \Cemm \textcolor{blue}{\bf t}^{\text{GHG}}$$, where the government decides the tax payable per unit emission. Finally, note that if $$\taxb$$ is non-zero, the objective is no longer linear. In such a case, we replace the product term with a McCormick relaxation.
\end{subequations}

The lower level Nash game that each producer $p$$ solves is as follow.
$$ \min  \qquad & \Cilin \qi + \frac{1}{2}\Ciquad {\qi}^2
      +\ti\qi
      -
      \left (
      \DemInt - \DemSlope \left(
    \sum_{p'\in\mathscr{P}} \qi[p'] + \qimp - \qexp
    \right)\qi
      \right )$$
$$  \text{s.t.} \qquad & \qi \geq  0 \qquad \qi \leq \qiCap $$
The first two terms in the objective correspond to the cost incurred by the energy producer, while the third term is the tax expense. The the parenthesis results in the revenue of $$p$$, which is the product of domestic price and the quantity produced. Further, the producer is constrained by their capacity limits. Note that the product of variables ($$\ti\qi$$) in the objective does not pose any additional difficulty to the problem. This is because the follower's problem is still convex quadratic for a {\em fixed} value of $$\ti$$ and the KKT conditions now give complementarity constraints with only linear terms.
