# finances

We can develop an individualized risk tolerance, h,
  characterized by a utility function over time, then
  h(u(y), t_p), where we can let t_p=0 correspond to the
  present time, and where the utility function is
  learned from the result of responses, y, to a set of
  questions asked of the individual. The questions that
  inform the utility function are generated as needed
  based on the responses to previous questions, in order
  to maximize the information gain of the next question
  with respect to t_p, thus the next question is
  q_prime{i+1} = argmax_{g} of g(y, q_{i+1}).
  The question generating function for possible q_{i+1}
  takes as inputs the set of previous responses,
  y to y_{i-1}, as well as a return generating function,
  which would be basically
  an auto-correlative daily Monte Carlo sampling of a
  LaPlacian function distribution, r(L(m,v), c, t), for t ranging
  in size by a number of increments relative to t_p,
  utilizing an auto-correlative constant, c, as the variance
  of white Gaussian noise used to transform L, which would
  be on the order of multiples of v, the variance of L.
  The function for q_{i+1} would be called recursively,
  with the best estimate for q_prime_{i+1} used to suggest
  the t_p and the return involved in q_{i+1}.
  The form of the questions would be combinations
  of return, risk, and time from the
  hypothetical present, t_h, are presented, such as,
  [
      y_i = q_i(r_h1, r_h2, s_h1, s_h2, t_h1, t_h2)
  ],
  where r_h1 is generated from r(L(m,v), c, t_h1), and
  the risk is that s_h1 and s_h2 are the probabilities of
  experiencing h1 and h2, and s_h1 + s_h2 = 1.
  Thus, y is essentially a Sharpe ratio.

  Net worth can be incorporated
  in the risk tolerance calculation, as part of the function
  aggregating u(y), to more appropriately
  explain some common actions that seem to go against
  utility theory - e.g. playing the lottery (even though
  it's a negative utility action, humans may not be
  able to distinguish such small changes to net worth
  such as an instance of a lottery playing loss).

The difference between t_p and t_h is relevant due to the
  individual's mortality. Thus, a relationship between t_p
  and t_h can be mapped, eg. from actuarial tables, which
  could, for instance, incorporate the current age of the
  respondent at t_p to account any possible indifference
  to a rational choice that would be likely to payoff
  over a sufficiently long time to t_h for a sufficiently
  old respondent.

Since people have a hard time abstractly judging
  probabilities that are close to either 0 or 1,
  most questions can utilize probabilities close
  to 0.5, where s_h1 ~= s_h2, or simply defined as
  absolutely 0 or 1, such that s_h1 != s_h2.
