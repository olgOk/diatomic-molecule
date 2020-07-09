"""Plot the VQE binding energy curve of a diatomic molecule from a Quantum Engine workflow result JSON."""

import json
from matplotlib import pyplot as plt

# Insert the path to your JSON file here
with open('87e1fcc2-6b5b-57a7-b4ae-72ba4887898a.json') as f:
    data = json.load(f)

# Extract lists of energies, bond lengths, and basis sets.
energies = []
bond_lengths = []
basis_sets = []
for task in data:
    if data[task]['class'] == 'optimize-variational-circuit':
        qubit_op = data[task]['inputArtifact:qubit-operator']
        qubit_op_creator = qubit_op.split('/')[0]
        interaction_op = data[qubit_op_creator]['inputArtifact:input-op']
        interaction_op_creator = interaction_op.split('/')[0]
        geometry = data[interaction_op_creator]['inputArtifact:geometry']
        geometry_creator = geometry.split('/')[0]
        bond_lengths.append(float(data[geometry_creator]['inputParam:bond-length']))
        energies.append(data[task]['optimization-results']['opt_value'])
        basis_sets.append(data[interaction_op_creator]['inputParam:basis'])

# Group the bond lengths and energies according to the basis set, and sort by
# bond length.
bond_length_sets = []
energy_sets = []
basis_set_list = list(set(basis_sets))
for basis in basis_set_list:
    indices = [i for i, x in enumerate(basis_sets) if x == basis]
    bond_length_sets.append([bond_lengths[i] for i in indices])
    energy_sets.append([energies[i] for i in indices])
    bond_length_sets[-1], energy_sets[-1] = zip(*sorted(zip(bond_length_sets[-1], energy_sets[-1]), key=lambda x: x[0]))

# Plot the binding energy curve
plt.figure()
for i in range(len(basis_set_list)):
    plt.plot(bond_length_sets[i], energy_sets[i], marker='o')

plt.xlabel('Bond length (Angstroms)')
plt.ylabel('Energy (Ha)')
plt.legend(basis_set_list)
plt.tight_layout()
plt.show()
