CELLTYPEMARKER_TOPOLOGIES = {
    "0.0.1": {
        "genome": "Mus_musculus_GRCm38_97",
        "hyper_parameters": {
            "l1_coef": 0.,
            "l2_coef": 0.,
            "kernel_initializer": 'glorot_uniform',
            "bias_initializer": 'zeros',
            "bias_regularizer": None,
            "kernel_constraint": None,
            "bias_constraint": None
        }
    }
}

# Load versions from extension if available:
try:
    import sfaira_extension
    CELLTYPEMARKER_TOPOLOGIES = {
        **CELLTYPEMARKER_TOPOLOGIES,
        **sfaira_extension.versions.topology_versions.mouse.celltype.CELLTYPEMARKER_TOPOLOGIES
    }
except ImportError:
    pass
