import numpy as np

angles = np.array([0, 30, 45, 60, 90])
angles_radians = angles * np.pi / 180
print(angles_radians)

print('Sine of angles in the array:')
print(np.sin(angles_radians))

angles_radians = np.radians(angles)
print(angles_radians)

print('Cosine of angles in the array:')
print(np.cos(angles_radians))

print('Tangent of angles in the array:')
print(np.tan(angles_radians))

sin = np.sin(angles * np.pi / 180)
arcsin = np.arcsin(sin)
print(arcsin)

print('Check result by converting to degrees:')
print(np.degrees(arcsin))
print('')

test_scores = np.array([32.32, 56.98, 21.52])
print(np.mean(test_scores))  # average
print(np.median(test_scores))  # median

