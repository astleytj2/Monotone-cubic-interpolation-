import math

x_coord = [1, 2, 3, 4, 5, 6, 7, 8, 9]
y_coord = [30, 28, 25, 10, 9, 8, 6, 2, 1]

# Step 1
delta_x = []
for k in range(0, len(x_coord) - 1):
    delta_x.append(x_coord[k + 1] - x_coord[k])
delta_y = []
for k in range(0, len(y_coord) - 1):
    delta_y.append(y_coord[k + 1] - y_coord[k])
delta_k = []
for k in range(0, len(delta_y)):
    delta_k.append(delta_y[k] / delta_x[k])

# Step 2
m_k = []
for k in range(1, len(delta_k)):
    m_k.append((delta_k[k - 1] + delta_k[k]) / 2)
m_k.append(delta_k[len(delta_k) - 1])
m_k.insert(0, delta_k[0])
# Needs line adding to check whether two consecutive values of delta_k have opposite signs.
# Then, if any do, replace that value of m_k with 0

# Step 3
# If delta_k = 0, set m_k = m_k+1 = 0 and ignore step 4 and 5 for these values

# Step 4
alpha_k = []
for k in range(0, len(delta_k)):
    alpha_k.append(m_k[k] / delta_k[k])
beta_k = []
for k in range(0, len(delta_k)):
    beta_k.append(m_k[k + 1] / delta_k[k])
# If either of these returns a negative, set m_k = 0 if alpha_k < 0, or m_k+1 = 0 if beta_k < 0

# Step 5
# condition a
phi_k = []
for k in range(0, len(alpha_k)):
    phi_k.append(alpha_k[k] - (((2 * alpha_k[k] + beta_k[k] - 3) * (2 * alpha_k[k] + beta_k[k] - 3)) / (
                3 * (alpha_k[k] + beta_k[k] - 2))))
# condition b
condition_b = []
for k in range(0, len(alpha_k)):
    condition_b.append(alpha_k[k] + (2 * beta_k[k]) - 3)
# condition c
condition_c = []
for k in range(0, len(alpha_k)):
    condition_c.append((2 * alpha_k[k]) + beta_k[k] - 3)

print("condition a: ", phi_k)
print("condition b: ", condition_b)
print("condition c: ", condition_c)

m_k2 = []
for k in phi_k:
    if k < 0:
        m_k2.append(3 * delta_k[phi_k.index(k)])
    else:
        m_k2.append(m_k[phi_k.index(k)])
m_k2.append(m_k[len(m_k)-1])


# This should check for whether the conditions hold first

a = []
for k in range(0, len(m_k2) - 1):
    a.append(delta_x[k] * delta_x[k] * delta_x[k] * ((2 * y_coord[k]) + (delta_x[k] * m_k2[k]) + (-2 * y_coord[k+1]) + (delta_x[k] * m_k2[k+1])))
b = []
for k in range(0, len(m_k2) - 1):
    b.append(delta_x[k] * delta_x[k] * ((-3 * y_coord[k]) + (-2 * delta_x[k] * m_k2[k]) + (3 * y_coord[k+1]) + (-1 * delta_x[k] * m_k2[k+1])))
c = []
for k in range(0, len(m_k2) - 1):
    c.append(delta_x[k] * delta_x[k] * m_k2[k])

print('a', a)
print('b', b)
print('c', c)


# The following assumes that known x coordinates are positive integers with a difference of 1
x = float(input("input x coordinate: "))
x_lower = math.floor(x)
x_upper = math.ceil(x)

f_int = (a[x_lower - 1] * ((x - x_lower) ** 3)) + (b[x_lower - 1] * ((x - x_lower) ** 2)) + (c[x_lower - 1] * (x - x_lower)) + y_coord[x_lower - 1]
print(f_int)

