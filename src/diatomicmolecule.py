"""Function for building a diatomic molecule."""

def create_diatomic_molecule_geometry(species1, species2, bond_length):
    """Create a molecular geometry for a diatomic molecule.

    Args:
        species1 (str): Chemical symbol of the first atom, e.g. 'H'.
        species2 (str): Chemical symbol of the second atom.
        bond_length (float): bond distance.

    Returns:
        dict: a dictionary containing the coordinates of the atoms.
    """

    geometry = {"sites": [
        {'species': species1, 'x': 0, 'y': 0, 'z': 0},
        {'species': species2, 'x': 0, 'y': 0, 'z': bond_length}
    ]}

    return geometry
