import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from numpy import array


if __name__ == "__main__":
    FRONT = np.array(
        [
            array([104.03218079, -3.2962471]),
            array([84.37215462, -3.2023968]),
            array([120.04474564, -3.48130786]),
            array([392.2849884, -12.21300316]),
            array([322.48522339, -6.92196517]),
            array([516.50812378, -26.63399944]),
            array([514.43743591, -26.61279602]),
            array([293.3130188, -5.84445581]),
            array([536.4914917, -27.62423553]),
            array([0.97490724, -0.48763287]),
            array([574.243573, -27.83850842]),
            array([558.38112793, -27.83377533]),
            array([303.31135864, -5.89489326]),
            array([0.69760801, -0.43695198]),
            array([315.12086792, -6.27541914]),
            array([582.8708374, -28.36918907]),
            array([487.62719421, -14.3553566]),
            array([316.31707458, -6.40442953]),
            array([320.11086731, -6.51013203]),
            array([303.98336792, -5.95369277]),
            array([316.20528564, -6.36589198]),
            array([479.37630615, -13.92314682]),
            array([309.28279724, -6.08373523]),
            array([1.28980447, -0.51973429]),
            array([487.38606873, -14.0391222]),
            array([310.22394409, -6.19741654]),
            array([0.98961216, -0.49730572]),
            array([634.72114868, -29.02197609]),
            array([478.62550659, -13.67044048]),
            array([309.29008789, -6.18930669]),
            array([493.55820312, -14.43126259]),
            array([313.54429932, -6.23890023]),
            array([499.79470825, -14.85618849]),
            array([648.51172485, -29.24445286]),
            array([469.12164307, -13.5911068]),
            array([650.73646851, -29.27178936]),
            array([631.85586548, -28.73960781]),
            array([291.90207825, -5.79208899]),
            array([466.20952759, -13.13414631]),
            array([286.01286011, -5.76650791]),
            array([666.06743164, -30.67761631]),
            array([478.88014221, -13.76264572]),
            array([677.56400757, -31.00341854]),
            array([662.05055542, -29.8184267]),
            array([467.84849243, -13.36830616]),
            array([305.19058533, -6.00012465]),
            array([594.53167114, -28.51274166]),
            array([457.26227722, -12.86975336]),
            array([482.93273315, -13.93237982]),
            array([464.7227417, -13.08966732]),
            array([495.48321838, -14.61671543]),
            array([490.02477722, -14.36430035]),
            array([320.57095337, -6.71295795]),
            array([479.21856079, -13.8685729]),
        ]
    )

    FRONT_SHARED_BUFF = np.array(
        [
            array([98.29978333, -4.46482792]),
            array([78.39651566, -3.68490503]),
            array([94.27448349, -4.31300168]),
            array([95.82668152, -4.39871058]),
            array([1.61362513, -0.54137954]),
            array([322.63112183, -7.92109909]),
            array([1.46118311, -0.50417168]),
            array([1.23563715, -0.49663126]),
            array([493.53623657, -31.76862698]),
            array([487.31108093, -31.62390766]),
            array([404.89170532, -14.23671722]),
            array([473.76793823, -30.71185436]),
            array([400.49285583, -9.0085146]),
            array([384.33553162, -8.31403818]),
            array([394.64042358, -8.61670589]),
            array([1.16336878, -0.48861307]),
            array([432.30697327, -15.21185322]),
            array([423.38805847, -14.27713633]),
            array([379.96637878, -8.11034994]),
            array([429.5090332, -14.35064478]),
            array([394.52761841, -8.61493454]),
            array([400.26083984, -8.70138197]),
            array([431.56075439, -14.6206398]),
            array([390.70614624, -8.39857893]),
            array([448.45429382, -15.22754126]),
            array([506.88987122, -32.96004753]),
            array([508.15516357, -33.10424652]),
            array([503.86594238, -32.40897903]),
            array([443.72345886, -15.21643209]),
            array([393.58842773, -8.5639761]),
            array([368.04249878, -7.98134418]),
            array([-0.34792859, -0.46243652]),
            array([463.93538513, -15.55277338]),
            array([457.6896698, -15.28752422]),
            array([465.40925293, -15.6051383]),
            array([0.32699837, -0.47935211]),
            array([-0.22501325, -0.46657244]),
            array([461.38174438, -15.49329157]),
            array([0.17694717, -0.47497972]),
            array([466.21352844, -15.92569923]),
            array([383.89640808, -8.16185751]),
            array([388.10532837, -8.36272802]),
        ]
    )

    FRONT_PSA_SHARED_BUFF = np.array(
        [
            array([176.26650391, -5.38293619]),
            array([209.06810608, -6.7399869]),
            array([197.33509827, -6.17592659]),
            array([187.75298004, -6.05156994]),
            array([208.73871765, -6.56659408]),
            array([299.34870911, -8.91197815]),
            array([292.69308167, -8.5279376]),
            array([269.76284485, -7.61365886]),
            array([282.08546143, -8.32610698]),
            array([366.4400177, -9.62000427]),
            array([337.46746826, -9.39943981]),
            array([1.48162409, -0.64178811]),
            array([1.76392555, -0.66295932]),
            array([342.502771, -9.58178215]),
            array([1.88899976, -0.68612376]),
            array([0.99291482, -0.48227457]),
            array([1.03664375, -0.51787066]),
            array([544.78585205, -16.50008392]),
            array([409.23789368, -10.56256533]),
            array([-0.2429284, -0.46802195]),
            array([421.79982605, -10.56720276]),
            array([409.14884644, -10.27843571]),
            array([401.40573425, -10.09329605]),
            array([404.6448761, -10.16228771]),
            array([569.88695679, -17.03537903]),
            array([449.35554199, -11.14580374]),
            array([0.4044235, -0.47430954]),
            array([428.13062439, -10.82679243]),
            array([574.69595337, -17.36814079]),
            array([566.70066528, -16.5107811]),
            array([446.85782166, -11.12556496]),
            array([455.05646057, -11.48170013]),
            array([442.56497803, -10.9458313]),
            array([460.49550171, -11.59460306]),
            array([577.09351807, -17.37910824]),
            array([452.09753113, -11.31301594]),
            array([462.14849243, -11.65219498]),
            array([467.72116089, -11.894876]),
            array([588.17702637, -17.44207706]),
            array([641.33065796, -19.44361553]),
            array([608.28724976, -18.25503387]),
            array([600.63127441, -17.65922585]),
            array([472.32736816, -11.90489578]),
            array([568.03542786, -16.98613453]),
            array([486.77310791, -12.36995945]),
            array([612.33746948, -19.00233402]),
            array([620.3713623, -19.37702827]),
            array([668.81870728, -21.77890053]),
            array([487.42298889, -13.50617418]),
            array([702.31272583, -22.95166607]),
            array([495.42462463, -13.63524179]),
            array([652.6093689, -20.30683022]),
            array([656.93498535, -21.03370247]),
            array([505.29367065, -14.3910594]),
            array([517.27693787, -14.87132206]),
            array([752.73759155, -32.28304386]),
            array([542.42202759, -15.66633997]),
            array([536.88441467, -15.48059025]),
            array([527.34212036, -15.06713438]),
            array([512.60548096, -14.54715748]),
            array([522.85482788, -15.01956987]),
            array([745.39812622, -28.09912128]),
            array([756.92436523, -32.37319603]),
            array([750.53161011, -29.23701839]),
            array([57.81000627, -3.08600403]),
            array([746.86820068, -28.98073997]),
            array([2.93328909, -1.71565214]),
            array([52.36709821, -3.08436387]),
            array([750.53635864, -32.12176037]),
            array([778.8944519, -32.71833439]),
            array([761.53973999, -32.45482845]),
            array([725.31375122, -26.34633198]),
            array([711.50366211, -25.86714077]),
        ]
    )

    dataframe_vanilla = pd.DataFrame(FRONT, columns=["distance", "energy"], index=FRONT[:, 0])
    dataframe_shared_buff = pd.DataFrame(FRONT_SHARED_BUFF, columns=["distance", "energy"], index=FRONT_SHARED_BUFF[:, 0])
    dataframe_shared_buff_PSA = pd.DataFrame(
        FRONT_PSA_SHARED_BUFF, columns=["distance", "energy"], index=FRONT_PSA_SHARED_BUFF[:, 0]
    )

    concatenated = pd.concat(
        [
            dataframe_vanilla.assign(variant="MORL/D vanilla"),
            # dataframe_shared_buff.assign(variant="shared_buffer"),
            dataframe_shared_buff_PSA.assign(variant="MORL/D-SB+PSA"),
        ]
    )
    sns.set(style="darkgrid")

    sns.scatterplot(concatenated, x="distance", y="energy", hue="variant", palette=["red", "blue"], alpha=0.6)
    plt.savefig("front_cheetah.png", dpi=400)
    plt.show()
