# Mathematical Verification — M3 Derivative Animation

## Function
f(x) = x²

## Point A
x₁ = 2  →  f(2) = 2² = 4  →  A = (2, 4)  ✓

## Point B (general)
x₂ = 2 + h  →  f(2+h) = (2+h)²  →  B = (2+h, (2+h)²)  ✓

## Secant Slope (Average Rate of Change)
slope = [f(2+h) − f(2)] / [(2+h) − 2]
      = [(2+h)² − 4] / h
      = [4 + 4h + h² − 4] / h
      = [4h + h²] / h
      = 4 + h  ✓

## Verification of Specific Secant Slopes

| h   | B = (2+h, (2+h)²) | slope = 4+h |
|-----|--------------------|-------------|
| 2   | (4, 16)            | 6           | ✓ |
| 1   | (3, 9)             | 5           | ✓ |
| 0.5 | (2.5, 6.25)        | 4.5         | ✓ |
| 0.1 | (2.1, 4.41)        | 4.1         | ✓ |

### Manual check for h = 2:
slope = (16 − 4) / (4 − 2) = 12 / 2 = 6  ✓

### Manual check for h = 1:
slope = (9 − 4) / (3 − 2) = 5 / 1 = 5  ✓

### Manual check for h = 0.5:
slope = (6.25 − 4) / (2.5 − 2) = 2.25 / 0.5 = 4.5  ✓

### Manual check for h = 0.1:
slope = (4.41 − 4) / (2.1 − 2) = 0.41 / 0.1 = 4.1  ✓

## Derivative via Limit Definition

f'(2) = lim(h→0) [f(2+h) − f(2)] / h

Step 1: Substitute f(x) = x²
      = lim(h→0) [(2+h)² − 2²] / h

Step 2: Expand (2+h)²
      = lim(h→0) [4 + 4h + h² − 4] / h

Step 3: Simplify numerator (4 − 4 = 0)
      = lim(h→0) [4h + h²] / h

Step 4: Factor h from numerator
      = lim(h→0) h(4 + h) / h

Step 5: Cancel h (valid because h → 0, h ≠ 0 in limit process)
      = lim(h→0) (4 + h)

Step 6: Evaluate the limit
      = 4 + 0
      = 4  ✓

## Tangent Line Equation

Using point-slope form:
  y − y₁ = m(x − x₁)

With point (2, 4) and slope m = 4:
  y − 4 = 4(x − 2)
  y − 4 = 4x − 8
  y = 4x − 4  ✓

### Verification: tangent line passes through A
  y(2) = 4(2) − 4 = 8 − 4 = 4  ✓  (matches A = (2,4))

### Verification: tangent line has correct slope
  dy/dx = 4  ✓  (matches f'(2) = 4)

## Cross-check with Power Rule
f(x) = x²  →  f'(x) = 2x  →  f'(2) = 2(2) = 4  ✓

All calculations in the animation are mathematically correct.
