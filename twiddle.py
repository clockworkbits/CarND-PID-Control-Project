import subprocess

def twiddle(tol=0.01): 
    p = [0.0, 0.0, 0.0]
    dp = [1.0, 1.0, 1.0]
    best_err = run(p)

    it = 0
    while sum(dp) > tol:
        print("Iteration {}, best error = {}, params = {}, dp = {}".format(it, best_err, p, dp))
        for i in range(len(p)):
            p[i] += dp[i]
            err = run(p)

            if err < best_err:
                best_err = err
                dp[i] *= 1.1
            else:
                p[i] -= 2 * dp[i]
                err = run(p)

                if err < best_err:
                    best_err = err
                    dp[i] *= 1.1
                else:
                    p[i] += dp[i]
                    dp[i] *= 0.9
        it += 1
    return p

def run(p):
    result = subprocess.run(['./pid', str(p[0]), str(p[1]), str(p[2]), '2500'], stdout=subprocess.PIPE)
    data = result.stdout.decode('utf-8')
    print("Error = " + data)
    return float(data)

twiddle(0.00002)

#for i in range(5):
#    result = subprocess.run(['./pid', '0.1', '0.0004', '0.9', '100'], stdout=subprocess.PIPE)
#    data = result.stdout.decode('utf-8')
#    print("Got result = " + data )