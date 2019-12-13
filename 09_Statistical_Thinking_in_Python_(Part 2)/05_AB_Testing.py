# A/B Test
# Used by organizations to see if a strategy change gives a better result

# Null Hypothesis of an A/B Test
# The Test Statistic is impervious to the change.

# The vote for the Civil Rights Act in 1964
# The Civil Rights Act of 1964 was one of the most important pieces of legislation ever passed in the USA. Excluding "present" and "abstain" votes, 153 House Democrats and 136 Republicans voted yea. However, 91 Democrats and 35 Republicans voted nay. Did party affiliation make a difference in the vote?

# To answer this question, you will evaluate the hypothesis that the party of a House member has no bearing on his or her vote. You will use the fraction of Democrats voting in favor as your test statistic and evaluate the probability of observing a fraction of Democrats voting in favor at least as small as the observed fraction of 153/244. (That's right, at least as small as. In 1964, it was the Democrats who were less progressive on civil rights issues.) To do this, permute the party labels of the House voters and then arbitrarily divide them into "Democrats" and "Republicans" and compute the fraction of Democrats voting yea.
# Construct arrays of data: dems, reps
dems = np.array([True] * 153 + [False] * 91)
reps = np.array([True] * 136 + [False] * 35)

def frac_yea_dems(dems, reps):
    """Compute fraction of Democrat yea votes."""
    frac = np.sum(dems) / len(dems)
    return frac

# Acquire permutation samples: perm_replicates
perm_replicates = draw_perm_reps(dems, reps, frac_yea_dems, size=10000)

# Compute and print p-value: p
p = np.sum(perm_replicates <= 153/244) / len(perm_replicates)
print('p-value =', p)
# This small p-value suggests that party identity had a lot to do with the voting. Importantly, the South had a higher fraction of Democrat representatives, and consequently also a more racist bias.

# A time-on-website analog
# It turns out that you already did a hypothesis test analogous to an A/B test where you are interested in how much time is spent on the website before and after an ad campaign. The frog tongue force (a continuous quantity like time on the website) is an analog. "Before" = Frog A and "after" = Frog B. Let's practice this again with something that actually is a before/after scenario.

# We return to the no-hitter data set. In 1920, Major League Baseball implemented important rule changes that ended the so-called dead ball era. Importantly, the pitcher was no longer allowed to spit on or scuff the ball, an activity that greatly favors pitchers. In this problem you will perform an A/B test to determine if these rule changes resulted in a slower rate of no-hitters (i.e., longer average time between no-hitters) using the difference in mean inter-no-hitter time as your test statistic. The inter-no-hitter times for the respective eras are stored in the arrays nht_dead and nht_live, where "nht" is meant to stand for "no-hitter time."

# Since you will be using your draw_perm_reps() function in this exercise, it may be useful to remind yourself of its call signature: draw_perm_reps(d1, d2, func, size=1) or even referring back to the chapter 3 exercise in which you defined it.
nht_dead = np.array([  -1,  894,   10,  130,    1,  934,   29,    6,  485,  254,  372, 81,  191,  355,  180,  286,   47,  269,  361,  173,  246,  492, 462, 1319,   58,  297,   31, 2970,  640,  237,  434,  570,   77, 271,  563, 3365,   89,    0,  379,  221,  479,  367,  628,  843, 1613, 1101,  215,  684,  814,  278,  324,  161,  219,  545,  715, 966,  624,   29,  450,  107,   20,   91, 1325,  124, 1468,  104, 1309,  429,   62, 1878, 1104,  123,  251,   93,  188,  983,  166, 96,  702,   23,  524,   26,  299,   59,   39,   12,    2,  308, 1114,  813,  887])
nht_live = np.array([ 645, 2088,   42, 2090,   11,  886, 1665, 1084, 2900, 2432,  750, 4021, 1070, 1765, 1322,   26,  548, 1525,   77, 2181, 2752,  127, 2147,  211,   41, 1575,  151,  479,  697,  557, 2267,  542,  392, 73,  603,  233,  255,  528,  397, 1529, 1023, 1194,  462,  583, 37,  943,  996,  480, 1497,  717,  224,  219, 1531,  498,   44, 288,  267,  600,   52,  269, 1086,  386,  176, 2199,  216,   54, 675, 1243,  463,  650,  171,  327,  110,  774,  509,    8,  197, 136,   12, 1124,   64,  380,  811,  232,  192,  731,  715,  226, 605,  539, 1491,  323,  240,  179,  702,  156,   82, 1397,  354, 778,  603, 1001,  385,  986,  203,  149,  576,  445,  180, 1403, 252,  675, 1351, 2983, 1568,   45,  899, 3260, 1025,   31,  100, 2055, 4043,   79,  238, 3931, 2351,  595,  110,  215,    0,  563, 206,  660,  242,  577,  179,  157,  192,  192, 1848,  792, 1693, 55,  388,  225, 1134, 1172, 1555,   31, 1582, 1044,  378, 1687, 2915,  280,  765, 2819,  511, 1521,  745, 2491,  580, 2072, 6450, 578,  745, 1075, 1103, 1549, 1520,  138, 1202,  296,  277,  351, 391,  950,  459,   62, 1056, 1128,  139,  420,   87,   71,  814, 603, 1349,  162, 1027,  783,  326,  101,  876,  381,  905,  156, 419,  239,  119,  129,  467])
nht = np.array([ 843, 1613, 1101,  215,  684,  814,  278,  324,  161,  219,  545, 715,  966,  624,   29,  450,  107,   20,   91, 1325,  124, 1468, 104, 1309,  429,   62, 1878, 1104,  123,  251,   93,  188,  983, 166,   96,  702,   23,  524,   26,  299,   59,   39,   12,    2, 308, 1114,  813,  887,  645, 2088,   42, 2090,   11,  886, 1665, 1084, 2900, 2432,  750, 4021, 1070, 1765, 1322,   26,  548, 1525, 77, 2181, 2752,  127, 2147,  211,   41, 1575,  151,  479,  697, 557, 2267,  542,  392,   73,  603,  233,  255,  528,  397, 1529, 1023, 1194,  462,  583,   37,  943,  996,  480, 1497,  717,  224, 219, 1531,  498,   44,  288,  267,  600,   52,  269, 1086,  386, 176, 2199,  216,   54,  675, 1243,  463,  650,  171,  327,  110, 774,  509,    8,  197,  136,   12, 1124,   64,  380,  811,  232, 192,  731,  715,  226,  605,  539, 1491,  323,  240,  179,  702, 156,   82, 1397,  354,  778,  603, 1001,  385,  986,  203,  149, 576,  445,  180, 1403,  252,  675, 1351, 2983, 1568,   45,  899, 3260, 1025,   31,  100, 2055, 4043,   79,  238, 3931, 2351,  595, 110,  215,    0,  563,  206,  660,  242,  577,  179,  157,  192, 192, 1848,  792, 1693,   55,  388,  225, 1134, 1172, 1555,   31, 1582, 1044,  378, 1687, 2915,  280,  765, 2819,  511, 1521,  745, 2491,  580, 2072, 6450,  578,  745, 1075, 1103, 1549, 1520,  138, 1202,  296,  277,  351,  391,  950,  459,   62, 1056, 1128,  139, 420,   87,   71,  814,  603, 1349,  162, 1027,  783,  326,  101, 876,  381,  905,  156,  419,  239,  119,  129,  467])
# Compute the observed difference in mean inter-no-hitter times: nht_diff_obs
nht_diff_obs = diff_of_means(nht_dead, nht_live)

# Acquire 10,000 permutation replicates of difference in mean no-hitter time: perm_replicates
perm_replicates = draw_perm_reps(nht_dead, nht_live, diff_of_means, size=10000)

# Compute and print the p-value: p
p = np.sum(perm_replicates <= nht_diff_obs) / len(perm_replicates)
print('p-val =', p)
# Your p-value is 0.0001, which means that only one out of your 10,000 replicates had a result as extreme as the actual difference between the dead ball and live ball eras. This suggests strong statistical significance. Watch out, though, you could very well have gotten zero replicates that were as extreme as the observed value. This just means that the p-value is quite small, almost certainly smaller than 0.001.

# Hypothesis test of Correlation
# Posit bull hyposthesis: the two varaibles are completely uncorrelated
# Simulate data assuming null hypothesis is true
# Use Pearson correlation, ? , as test statistic
# Compute p-value as fraction of replicates that have ? at least as large as observed.

# # Hypothesis test on Pearson correlation
# The observed correlation between female illiteracy and fertility may just be by chance; the fertility of a given country may actually be totally independent of its illiteracy. You will test this hypothesis. To do so, permute the illiteracy values but leave the fertility values fixed. This simulates the hypothesis that they are totally independent of each other. For each permutation, compute the Pearson correlation coefficient and assess how many of your permutation replicates have a Pearson correlation coefficient greater than the observed one.

# The function pearson_r() that you wrote in the prequel to this course for computing the Pearson correlation coefficient is already in your name space.
# Compute observed correlation: r_obs
r_obs = pearson_r(illiteracy, fertility)

# Initialize permutation replicates: perm_replicates
perm_replicates = np.empty(10000)

# Draw replicates
for i in range(10000):
    # Permute illiteracy measurments: illiteracy_permuted
    illiteracy_permuted = np.random.permutation(illiteracy)

    # Compute Pearson correlation
    perm_replicates[i] = pearson_r(illiteracy_permuted, fertility)

# Compute p-value: p
p = np.sum(perm_replicates >= r_obs) / len(perm_replicates)
print('p-val =', p) # 0.0

# You got a p-value of zero. In hacker statistics, this means that your p-value is very low, since you never got a single replicate in the 10,000 you took that had a Pearson correlation greater than the observed one. You could try increasing the number of replicates you take to continue to move the upper bound on your p-value lower and lower.

# Do neonicotinoid insecticides have unintended consequences?
# As a final exercise in hypothesis testing before we put everything together in our case study in the next chapter, you will investigate the effects of neonicotinoid insecticides on bee reproduction. These insecticides are very widely used in the United States to combat aphids and other pests that damage plants.

# In a recent study, Straub, et al. (Proc. Roy. Soc. B, 2016) investigated the effects of neonicotinoids on the sperm of pollinating bees. In this and the next exercise, you will study how the pesticide treatment affected the count of live sperm per half milliliter of semen.

# First, we will do EDA, as usual. Plot ECDFs of the alive sperm count for untreated bees (stored in the Numpy array control) and bees treated with pesticide (stored in the Numpy array treated).
# Compute x,y values for ECDFs
x_control, y_control = ecdf(control)
x_treated, y_treated = ecdf(treated)

# Plot the ECDFs
plt.plot(x_control, y_control, marker='.', linestyle='none')
plt.plot(x_treated, y_treated, marker='.', linestyle='none')

# Set the margins
plt.margins(0.02)

# Add a legend
plt.legend(('control', 'treated'), loc='lower right')

# Label axes and show plot
plt.xlabel('millions of alive sperm per mL')
plt.ylabel('ECDF')
plt.show()
# The ECDFs show a pretty clear difference between the treatment and control; treated bees have fewer alive sperm. Let's now do a hypothesis test in the next exercise.

# Bootstrap hypothesis test on bee sperm counts
# Now, you will test the following hypothesis: On average, male bees treated with neonicotinoid insecticide have the same number of active sperm per milliliter of semen than do untreated male bees. You will use the difference of means as your test statistic.

# For your reference, the call signature for the draw_bs_reps() function you wrote in chapter 2 is draw_bs_reps(data, func, size=1).
# Compute the difference in mean sperm count: diff_means
diff_means = np.mean(control) - np.mean(treated)

# Compute mean of pooled data: mean_count
mean_count = np.mean(np.concatenate((control,treated)))

# Generate shifted data sets
control_shifted = control - np.mean(control) + mean_count
treated_shifted = treated - np.mean(treated) + mean_count

# Generate bootstrap replicates
bs_reps_control = draw_bs_reps(control_shifted,
                       np.mean, size=10000)
bs_reps_treated = draw_bs_reps(treated_shifted,
                       np.mean, size=10000)

# Get replicates of difference of means: bs_replicates
bs_replicates = bs_reps_control - bs_reps_treated

# Compute and print p-value: p
p = np.sum(bs_replicates >= np.mean(control) - np.mean(treated)) \
            / len(bs_replicates)
print('p-value =', p)
 # The p-value is small, most likely less than 0.0001, since you never saw a bootstrap replicated with a difference of means at least as extreme as what was observed. In fact, when I did the calculation with 10 million replicates, I got a p-value of 2e-05.