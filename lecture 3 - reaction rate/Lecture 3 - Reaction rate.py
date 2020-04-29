#!/usr/bin/env python
# coding: utf-8

# <!--NOTEBOOK_HEADER-->
# **Do we need to add this?**
# 
# *This notebook contains course material from [CBE20255](https://jckantor.github.io/CBE20255)
# by Jeffrey Kantor (jeff at nd.edu); the content is available [on Github](https://github.com/jckantor/CBE20255.git).
# The text is released under the [CC-BY-NC-ND-4.0 license](https://creativecommons.org/licenses/by-nc-nd/4.0/legalcode),
# and code is released under the [MIT license](https://opensource.org/licenses/MIT).*

# # Lecture 3 - Reaction rates

# ## Objectives
#    
# ### Define:
# * reaction rate
# * reation rate law
# * reation rate constant (k)
# * reaction order
# * overall order
# 
# ### Calculation:
# * calculating reaction rate for the reaction and rate of formation of compounds
# * calculating reaction extent
# * determining reaction order and rate constant from kinetic data

# ## Describing reaction rate

# Reaction rate shows the different rates of production of different species although we want an overall common rate to describe the system.
# 
# Say we have reaction $$A + 2B → 3C + D$$
# 
# Reaction rate can be calculated by:

# <p style="text-align:center;">
# <img src="Capture-reaction rate equation.PNG" width=700>
# </p>

# Reaction rate can also be found from the graph of concentration of components in the system vs. time:

# <p style="text-align:center;">
# <img src="Capture-reaction rate from graph.PNG" width=600>
# </p>

# ### Example
# 
# If we have the reaction 
# 
# $$ 2 NOBr_{(g)} ⇌ 2 NO_{(g)} + Br_{2(g)}$$
# 
# and we measure that the rate of formation of NO is 1.6 mmol/(L·s), what is the reation rate and the rate of formation of $Br_{2}$ and $NOBr$?

# <details>
#   <summary><font color='blue'>Click here to see the solution!</font></summary>
#     
# 
# >**Solution**
# >
# > **Step 1**: Determine the reaction rate from the rate of formation for NO. Rate of formation is already given in mmol/(L·s), so no need to convert. If given in mmol/s need to divide by volume.
# >\begin{align*}
# r & = \frac{1}{\nu_{j}} \frac{d[NO]}{dt} \\
# & = \frac{1}{2} \left( 1.6 \frac{mmol}{L·s}\right)\\
# & = 0.8\frac{mmol}{L·s}
# \end{align*}
# >
# >**Step 2**: Use the reacction rate to determine rate of formation for the other compounds
# >* rate of formation is positive for products and negative for reactants
# >\begin{align*}
# \frac{d[Br_{2}]}{dt}& = r \\
# & = 0.8\frac{mmol}{L·s}
# \end{align*}
# >\begin{align*}
# \frac{d[NOBr]}{dt}& = -2r \\
# & = -1.6\frac{mmol}{L·s}
# \end{align*}
#     
# </details>
# 
# 

# ## Extent of reaction

# We use the extent of reaction ($\xi$) to describe the change in an amount of a reacting speicies J.

# <p style><font color='red',size=3>$$d n_{j} = \nu_{j} d\xi$$</font>
#     
# where:
# >$dn_{j}$     = change in the number of moles of a certain substance
# >
# >$\nu_{j}$    = the stoichiometric corfficient
# >
# >$d\xi$    = the extent of reaction

# We can get a relationship between the reaction extent and the rate of reaction when the volume is constant:
# 
# <font color='red'>$$ r = \frac{1}{V} \frac{d\xi}{dt}  = \frac{1}{\nu_{j}} \frac{1}{V} \frac{d\xi}{dt}$$</font>
# 
# where:
# >$V$= volume

# ## Reaction rate law

# **Definition:** The relationship between The rate of reaction and the concentration of reactants.

# Rate law is generally found to be proportional to the concentrations of reactants raised to a power:
# 
# The general form for reaction rate law is 
# <font color='red'>$$r=k_{r}[A]^a[B]^b$$</font>
# 
# For gas cases we can use patial pressure
# <font color='red'>$$r=k_{r}p_{A}^a p_{B}^b$$</font>
# 
# The reaction constant $k_{r}$ is independent on concentration but dependent on temperature.  
# <br/><br/><br/>

# For example, the rate of the gas-phase decomposition of dinitrogen pentoxide,
# 
# $$ 2 N_{2}O_{5} ⇌ 4 NO_{2} + O_{2}$$
# 
# The rate law is found to be directly proportional to the concentration of $N_{2}O_{5}$:
# 
# $$ r = k_{r} [N_{2}O_{5}]$$
# 
# Reaction rate laws can be complicated and may tell us about the mechanism of the reactions. For example, the reaction between hydrogen and bromine:
# 
# Simple stoichiometry: $ H_{2(g)} + Br_{2(g)} → 2 HBr_{(g)}$
# 
# Complicated rate law: $$ r = \frac{k_{a}[H_{2}][Br_{2}]^{3/2}}{[Br_{2}]+k_{b}[HBr]}$$

# >### Rate law vs. Equilibrium constant
# Care must be taken not to confuse equilibrium constant expressions with rate law expressions. The expression for  $K_{eq}$  can always be written by inspecting the **balanced** reaction equation and contains a term for each species of the reaction (raised to the power of its coefficient) whose concentration changes during the reaction. The equilibrium constant for the above reaction is given below:
# >
# >$$K_{eq}=\frac{[NO_{2}]^4[O_{2}]}{[N_{2}O_{5}]^2}$$
# >
# >In contrast, the expression for the rate law generally bears no relation to the reaction equation, and must be determined experimentally.

# ## Reaction rate units

# Reaction rate(r) is always expressed in units of concentration over time.(e.g. <font size=3>$\frac{mol}{L·s}$, $\frac{kPa}{min}$, $\frac{mol}{m^3·h}$ </font>)
# 
# This means the rate constant $k_{r}$ needs to be such that r is expressed in units of concentration over time.

# ### Example
# 
# For the following example, what are the units for the reaction rate constant ($k_{r}$)?
# 
# $$r=k_{r}*p_{A}*p_{B}^2$$
# with unit for p as Pa and time in seconds

# <details>
#   <summary><font color='blue'>Click here to see the solution!</font></summary>
#     
# > **Solution**
# >
# > r is expressed in concentration over time, so the unit of r is $\frac{Pa}{s}$.
# >
# > $$\frac{Pa}{s} = k_{r}*Pa*Pa^2$$
# >$$k_{r}=\frac{1}{Pa^2s} $$
#     
# </details>
# 

# ## Reaction order

# The dependence of the rate of reaction on the reactant concentrations can often be expressed as a direct proportionality, in which the concentrations may be raised to be the zeroth, first, or second power. The exponent is known as the order of the reaction with respect to that substance.
# 
# The overall order of a reaction is the sum of the orders with respect to the sum of the exponents
# 
# For example: $$r = k_{r}[A]^3[B]^{1/2}$$
# The reaction is
# 
# >Third order in A
# >
# >One half order in B
# >
# >Three and a half order overall

# In the more complicated example for the reaction between hydrogen and bromine:
# 
# $$ r = \frac{k_{a}[H_{2}][Br_{2}]^{3/2}}{[Br_{2}]+k_{b}[HBr]}$$
# 
# The reaction is 
# >First order in $H_{2}$
# >
# >Indeterminate order in $Br_{2}$ (as it's not in a signle term)
# >
# >Indeterminate order in $HBr$ (as it cannot be isolated to a single term raised to a power)
# >
# >Indeterminate order overall (as some orders are indeterminate)

# ### Isolation method determining rate law

# One of the simplest methods for determining the rate law is the isolation method. 
# 
# Say we have a reaction with two reactants, A and B. We'll put a large amount of B in our reactor compared to A, so much that the concentration barely changes.
# 
# If the true rate law is: $r = k_{r}[A][B]^2$
# 
# What we would observe is $r = k_{eff}[A]$, where $k_{eff}=k_{r}[B_{0}]^2$
# >$k_{eff}$ = the effective rate constant 
# >
# >$[B_{0}]$ indicating the concentration of B at time 0 or also called B naught meaning nothing

# <p style="text-align:center;">
# <img src="Capture-isolation method reaction order.PNG" width=800>
# </p>

# With B in great excess: $r = k_{eff}[A]$ where $k_{eff}=k_{r}[B_{0}]^2$, reaction appears first order.
# 
# With A in great excess: $r = k'_{eff}[A]$ where $k'_{eff}=k_{r}[A_{0}]^2$, reaction appears second order.
# 
# >$k'_{eff}$ is read as k prime effective
# 
# It is easier to analyse these effective rate laws than the more complex combined rate law.

# ### Method of initial rates
# 
# The method of initial rates is commonly used in conjunction with the isolation methods to determine reaction order.

# **Example**
# 
# Say we have a reaction with two species, A and B. We put in a large excess of B into the reactor. The following as our initial rates are observed with different concentrations of A, what is th reaction order in A?
# 
# | [A] (mol/L) | Initial rate(mol/L·s) |
# | :---: | :--: |
# |     1     | $1×10^{-2}$ |
# |     2     | $4×10^{-2}$ |

# <details>
#   <summary><font color='blue'>Click here to see the solution!</font></summary>
#     
# > **Solution**
# >
# > As the concentration of A doubles, the reaction rate quadruples    $$r_{0}=k_{eff}[A]^2$$
# >
# > So the reaction is second order in A. 
#     
# </details>

# If we take the logarithm of the general equation, we can linearized the equation:
# 
# \begin{align*}
# r_{0} & = k_{eff}[A_{0}]^a \\
# log(r_{0})& = log(k_{eff}) + a*log([A_{0}])\\
# y & = intercept + slope * x
# \end{align*}
# 
# > Plot $log(r_{0})$ vs $log([A_{0}])$, where the slope is the reaction order in A; and y-intercept equals to  $log(k_{eff})$

# **Example**
# 
# Sulfuryl chloride ($SO_{2}Cl_{2}$) decomposes to $SO_{2}$ and $Cl_{2}$ by the following reaction:
# 
# $$SO_{2}Cl_{2(g)} → SO_{2(g)}+Cl_{2(g)}$$
# Data for the reaction at 320°C are listed in the following table. Calculate the reaction order with regard to sulfuryl chloride and determine the rate constant for the reaction.
# 
# | Experiment |   $[SO_{2}Cl_{2}]_{0}$ (M)   | Initial rate(M·s) |
# | :---: | :--: | :--: |
# |     1     |   0.0050   |$1.10×10^{-7}$ |
# |     2     |   0.0075   |$1.65×10^{-7}$ |
# |     3     |   0.0100   |$2.20×10^{-7}$ |
# |     4     |   0.0125   |$2.75×10^{-7}$ |

# <details>
#   <summary><font color='blue'>Click here to see the solution!</font></summary>
#     
# > **Solution**
# >
# >**Step 1**: determine the reaction order with respect to nitrogen dioxide
# >
# >Comparing Experiments 1 and 3, for example, shows that doubling the concentration doubles the reaction rate 
# >$(2.20×10^{-7}) ÷ (1.10×10^{-7}) = 2.0$, which means that the reaction rate is proportional to $[SO_{2}Cl_{2}]$.
# >    
# >The reaction is first order with respect to $SO_{2}Cl_{2}$. 
# >
# >**Step 2**: calculate $k_{r}$
# >
# >We have $rate = k_{r}[SO_{2}Cl_{2}]$. We can calculate the rate constant ($k_{r}$) using data from any experiment in the table.
# >\begin{align*}
# rate & = k_{r}[SO_{2}Cl_{2}] \\
# 1.10×10^{-7} M/s& = k_{r}×0.0050M \\
# 2.2×10^{-5}s^{-1} & = k_{r}
# \end{align*}
# >
# >
# >**Method 2**
# >
# > The following graph is produced when plotting $log(r_{0})$ vs $log([A_{0}])$
# > <p style="text-align:center;">
# ><img src="Capture- reaction order example.PNG" width=500>
# ></p>    
# >From the line of best fit, we can see a=1, $log(k_{r})=-4.6576$
# >
# >Therefore the reaction is first order in $SO_{2}Cl_{2}$, $k_{r}=10^{-4.6576} = 2.2×10^{-5}s^{-1}$.     
# </details>

# **Example**
# 
# At high temperatures, nitrogen dioxide decomposes to nitric oxide and oxygen.
# 
# $$2NO_{2(g)}−→2NO_{(g)}+O_{2(g)}$$
# 
# Experimental data for the reaction at 300°C and four initial concentrations of NO2 are listed in the following table:
# 
# | Experiment |   $$[NO_{2}]_{0}$$(M) | Initial rate(M·s) |
# | :---:  |  :--:  | :--: |
# |     1     |    0.015    |$$1.22×10^{-4}$$  |
# |     2     |    0.010    |$$5.40×10^{-5}$$ |
# |     3     |    0.0080    |$$3.46×10^{-5}$$ |
# |     4     |    0.0050    |$$1.35×10^{-5}$$ |
# 
# Determine the reaction order and the rate constant.

# <details>
# <summary><font color='blue'>Click here to see the solution!</font></summary>
#     
# > **Solution**
# >
# >**Step 1**: determine the reaction order with respect to nitrogen dioxide
# >
# >Comparing Experiments 2 and 4, for example, shows that doubling the concentration quadruples the reaction rate 
# >$(5.40 × 10^{−5}) ÷ (1.35 × 10^{−5}) = 4.0$, which means that the reaction rate is proportional to $[NO_{2}]^2$.
# >
# >Similarly, comparing Experiments 1 and 4 shows that tripling the concentration increases the reaction rate by a factor of 9, again indicating that the reaction rate is proportional to $[NO_{2}]^2$.
# >
# >Therefore, the reaction is second order with respect to nitrogen dioxide.
# >
# >**Step 2**: calculate $k_{r}$
# >
# >We have $rate = k_{r}[NO_{2}]^2$. We can calculate the rate constant ($k_{r}$) using data from any experiment in the table.
# >\begin{align*}
# rate & = k_{r}[NO_{2}]^2 \\
# 5.40×10^{-5} M/s& = k_{r}×(0.010M)^2\\
# 0.54M^{-1}s^{-1} & = k_{r}
# \end{align*}
# >    
# >
# >**method 2**
# >
# > The following graph is produced when plotting $log(r_{0})$ vs $log([A_{0}])$
# > <p style="text-align:center;">
# ><img src="Capture- reaction order example 2.PNG" width=500>
# ></p>    
# >From the line of best fit, we can see a=2, $log(k_{r})=-0.2602$
# >
# >Therefore the reaction is first order in $NO_{2}$, $k_{r}=10^{-0.2602} = 0.55 M^{-1}s^{-1}$.   
# </details>

# ## Integrated rate laws 

# Rate laws are differential equations can be integrated to find how the concentrations of reactants and products change with time. We can imagine a fairly complex system with multiple reactions described by
# 
# $$𝑟_{1}=𝑘_{𝑟1}∗𝑓(𝐴,𝐵,...),   𝑟_{2}=𝑘_{𝑟2}∗𝑓(𝐴,𝐵,...),    𝑟_{3},   𝑟_{4}....$$
# 
# Concentration of all components can be described by equations such as: $𝑑𝐴𝑑𝑡=−𝑟_{1}−2𝑟_{2}...$, we need to integrate these to find concentrations at a given time.
# 
# Any of these rate laws can be solved numerically (you’ll learn about this in CHBE 230). But some simpler cases can also be solved analytically.

# ## Zeroth order reactions
# 
# A zeroth-order reaction is one whose rate is independent of concentration; its differential rate law is
# 
# $$r=-\frac{d[A]}{dt}=k_{r}$$
# 
# Integrating from t=0 we have $[A]_{0}$ to some time t where we have $[A]$
# 
# $$\int_{[A]_{0}}^{[A]} \mathrm d[A] = \int_{t_{0}=0}^{t} \mathrm -k_{r}$$
# 
# 
# <p style="text-align:center;"><font color='red'>$[A]-[A]_{0}=-k_{r}*t$</font> or <font color='red'>$[A]=[A]_{0}-k_{r}*t$</font>

# <p style="text-align:center;">
# <img src="zeroth order reaction.PNG" width=600>
# </p>

# ## First order reactions
# 
# Doing a similar approach as with the zeroth order reactions:
# 
# $$r=-\frac{d[A]}{dt}=k_{r}[A]$$
# 
# $$\int_{[A]_{0}}^{[A]} \frac{d[A]}{[A]} = \int_{t_{0}=0}^{t} \mathrm-k_{r}$$
# 
# 
# <p style="text-align:center;"> <font color='red',size=3>$ln[A]-ln[A]_{0}=-k_{r}*t$</font> or <font color='red',size=3>$[A]=[A]_{0}e^{-k_{r}*t}$</font>
# <br/><br/>

# <p style="text-align:center;">
# <img src="first order reaction.PNG" width=900>
# </p>

# Based on the equation we found, what is an expression for the time taken for half of A to be consumed (half-life)?
# 
# $$ln[A]-ln[A]_{0}=-k_{r}*t$$
# 
# \begin{align*}
# k_{r}* t_{1/2} & = -ln \frac{[A]}{[A]_{0}} \\
# & = -ln \frac{\frac{1}{2}[A]_{0}}{[A]_{0}} \\
# & =-ln(\frac{1}{2}) \\
# & = ln(2)
# \end{align*}
# 
# <font color='red'>$$t_{1/2}=\frac{ln(2)}{k_{r}}$$</font> 
# <p style="text-align:center;">Note that this half life does not depend on [A].
#     
# **Practice**: use $[A]=[A]_{0}e^{-k_{r}*t}$, you should get the same result.

# <details>
# <summary><font color='blue'>Click here to see the solution!</font></summary>
#     
# > **Solution**
# >\begin{align*}
# [A] & = [A]_{0}*e^{-k_{r}t_{1/2}} \\
# \frac{[A]}{[A]_{0}}& = e^{-k_{r}t_{1/2}} \\
# \frac{1}{2} & = e^{-k_{r}t_{1/2}} \\
# ln(\frac{1}{2}) & = -k_{r}*t_{1/2}
# \end{align*} 
# >
# > $$t_{1/2} =-\frac{ln(\frac{1}{2})}{k_{r}} = \frac{ln(2)}{k_{r}}$$
#     
# </details>

# ## Second order reactions
# 
# $$r=-\frac{d[A]}{dt}=k_{r}[A]^2$$
# 
# $$\int_{[A]_{0}}^{[A]} \frac{d[A]}{[A]^2} = \int_{t_{0}=0}^{t} \mathrm-k_{r}$$
# 
# <p style="text-align:center;"> <font color='red',size=4>$\frac{1}{[A]}-\frac{1}{[A]_{0}}=k_{r}*t$</font> or <font color='red',size=4>$[A]=\frac{[A]_{0}}{1+k_{r}*t*[A]_{0}}$</font>
#    
# <p style>Using this to find half life, we find that: <font color='red',size=4> $t_{1/2}=\frac{1}{k_{r}*[A]_{0}}$ </font>

# <p style="text-align:center;">
# <img src="second order reaction.PNG" width=800>
# </p>

# In[ ]:





# In[ ]:





# In[ ]:




