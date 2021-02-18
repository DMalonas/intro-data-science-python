def chickenpox_by_sex():
    # YOUR CODE HERE
    # raise NotImplementedError()
    import pandas as pd
    import numpy as np
    df = pd.read_csv("assets/NISPUF17.csv", index_col=0)

    cpo_sex = df[df['P_NUMVRC'].gt(0) & df['HAD_CPOX'].lt(3)].loc[:, ['HAD_CPOX', 'SEX']]
    # Male 1 Female 2
    cpo1_sex1 = len(cpo_sex[(cpo_sex['HAD_CPOX'] == 1) & (cpo_sex['SEX'] == 1)])
    cpo1_sex2 = len(cpo_sex[(cpo_sex['HAD_CPOX'] == 1) & (cpo_sex['SEX'] == 2)])
    cpo2_sex1 = len(cpo_sex[(cpo_sex['HAD_CPOX'] == 2) & (cpo_sex['SEX'] == 1)])
    cpo2_sex2 = len(cpo_sex[(cpo_sex['HAD_CPOX'] == 2) & (cpo_sex['SEX'] == 2)])

    cbs = {"male": cpo1_sex1 / cpo2_sex1, "female": cpo1_sex2 / cpo2_sex2}

    return cbs
