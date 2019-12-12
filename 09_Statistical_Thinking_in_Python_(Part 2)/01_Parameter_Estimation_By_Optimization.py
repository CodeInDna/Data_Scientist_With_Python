# Optimal parameters
# Parameter values that bring the model in closest agreement with the data.

# How often do we get no-hitters?
# The number of games played between each no-hitter in the modern era (1901-2015) of Major League Baseball is stored in the array nohitter_times.

# If you assume that no-hitters are described as a Poisson process, then the time between no-hitters is Exponentially distributed. As you have seen, the Exponential distribution has a single parameter, which we will call τ, the typical interval time. The value of the parameter τ that makes the exponential distribution best match the data is the mean interval time (where time is in units of number of games) between no-hitters.

# Compute the value of this parameter from the data. Then, use np.random.exponential() to "repeat" the history of Major League Baseball by drawing inter-no-hitter times from an exponential distribution with the τ you found and plot the histogram as an approximation to the PDF.

# NumPy, pandas, matlotlib.pyplot, and seaborn have been imported for you as np, pd, plt, and sns, respectively.
nohitter_items = np.array([ 843, 1613, 1101,  215,  684,  814,  278,  324,  161,  219,  545, 715,  966,  624,   29,  450,  107,   20,   91, 1325,  124, 1468, 104, 1309,  429,   62, 1878, 1104,  123,  251,   93,  188,  983, 166,   96,  702,   23,  524,   26,  299,   59,   39,   12,    2, 308, 1114,  813,  887,  645, 2088,   42, 2090,   11,  886, 1665, 1084, 2900, 2432,  750, 4021, 1070, 1765, 1322,   26,  548, 1525, 77, 2181, 2752,  127, 2147,  211,   41, 1575,  151,  479,  697, 557, 2267,  542,  392,   73,  603,  233,  255,  528,  397, 1529, 1023, 1194,  462,  583,   37,  943,  996,  480, 1497,  717,  224, 219, 1531,  498,   44,  288,  267,  600,   52,  269, 1086,  386, 176, 2199,  216,   54,  675, 1243,  463,  650,  171,  327,  110, 774,  509,    8,  197,  136,   12, 1124,   64,  380,  811,  232, 192,  731,  715,  226,  605,  539, 1491,  323,  240,  179,  702, 156,   82, 1397,  354,  778,  603, 1001,  385,  986,  203,  149, 576,  445,  180, 1403,  252,  675, 1351, 2983, 1568,   45,  899, 3260, 1025,   31,  100, 2055, 4043,   79,  238, 3931, 2351,  595, 110,  215,    0,  563,  206,  660,  242,  577,  179,  157,  192, 192, 1848,  792, 1693,   55,  388,  225, 1134, 1172, 1555,   31, 1582, 1044,  378, 1687, 2915,  280,  765, 2819,  511, 1521,  745, 2491,  580, 2072, 6450,  578,  745, 1075, 1103, 1549, 1520,  138, 1202,  296,  277,  351,  391,  950,  459,   62, 1056, 1128,  139, 420,   87,   71,  814,  603, 1349,  162, 1027,  783,  326,  101, 876,  381,  905,  156,  419,  239,  119,  129,  467])

# Seed random number generator
np.random.seed(42)

# Compute mean no-hitter time: tau
tau = np.mean(nohitter_times)

# Draw out of an exponential distribution with parameter tau: inter_nohitter_time
inter_nohitter_time = np.random.exponential(tau, 100000)

# Plot the PDF and label axes
_ = plt.hist(inter_nohitter_time,
             bins = 50, normed=True,histtype='step')
_ = plt.xlabel('Games between no-hitters')
_ = plt.ylabel('PDF')

# Show the plot
plt.show()
#  We see the typical shape of the Exponential distribution, going from a maximum at 0 and decaying to the right.

# Do the data follow our story?
# You have modeled no-hitters using an Exponential distribution. Create an ECDF of the real data. Overlay the theoretical CDF with the ECDF from the data. This helps you to verify that the Exponential distribution describes the observed data.

# It may be helpful to remind yourself of the function you created in the previous course to compute the ECDF, as well as the code you wrote to plot it.
# Create an ECDF from real data: x, y
x, y = ecdf(nohitter_times)

# Create a CDF from theoretical samples: x_theor, y_theor
x_theor, y_theor = ecdf(inter_nohitter_time)

# Overlay the plots
plt.plot(x_theor, y_theor)
plt.plot(x, y, marker='.', linestyle='none')

# Margins and axis labels
plt.margins(0.02)
plt.xlabel('Games between no-hitters')
plt.ylabel('CDF')

# Show the plot
plt.show()
# It looks like no-hitters in the modern era of Major League Baseball are Exponentially distributed. Based on the story of the Exponential distribution, this suggests that they are a random process; when a no-hitter will happen is independent of when the last no-hitter was.

# How is this parameter optimal?
# Now sample out of an exponential distribution with τ being twice as large as the optimal τ. Do it again for τ half as large. Make CDFs of these samples and overlay them with your data. You can see that they do not reproduce the data as well. Thus, the τ you computed from the mean inter-no-hitter times is optimal in that it best reproduces the data.

# Note: In this and all subsequent exercises, the random number generator is pre-seeded for you to save you some typing.
# Plot the theoretical CDFs
plt.plot(x_theor, y_theor)
plt.plot(x, y, marker='.', linestyle='none')
plt.margins(0.02)
plt.xlabel('Games between no-hitters')
plt.ylabel('CDF')

# Take samples with half tau: samples_half
samples_half = np.random.exponential(tau/2,size=10000)

# Take samples with double tau: samples_double
samples_double = np.random.exponential(2*tau,size=10000)

# Generate CDFs from these samples
x_half, y_half = ecdf(samples_half)
x_double, y_double = ecdf(samples_double)

# Plot these CDFs as lines
_ = plt.plot(x_half, y_half)
_ = plt.plot(x_double, y_double)

# Show the plot
plt.show()

# Linear regression by least squares
# Least Squares
# The process of finding the parameteres for which the sum of the squares of the residuals is minimal.