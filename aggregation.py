import matplotlib.pyplot as plt
import numpy as np

matrix=np.array([[0.13432897, 0.10467831, 0.09387882, 0.11714209, 0.09367946 ,0.11181255,
  0.1388388 , 0.07898296, 0.12894433, 0.07365164, 0.1232618 ],
 [0.12025822, 0.13662158, 0.11562019, 0.1517003 , 0.09161258 ,0.09058445,
  0.0998572 , 0.11051208, 0.12047933, 0.10308096, 0.09550465],
 [0.13198118, 0.12337274, 0.14456654, 0.08401143, 0.14503296 ,0.064728,
  0.08708661, 0.08021203, 0.08349928, 0.10111966, 0.10743899],
 [0.08229061, 0.08321807, 0.13000245, 0.07052068, 0.07072631 ,0.14943933,
  0.09930748, 0.13679881, 0.07152302, 0.11685744, 0.07387507],
 [0.14455918, 0.10858378, 0.06670126, 0.09295374, 0.07512063 ,0.13202776,
  0.07231505, 0.08961164, 0.07525839, 0.11900142, 0.11651812],
 [0.15264112, 0.0821522 , 0.09633323, 0.08283599, 0.14049138 ,0.05547365,
  0.1547993 , 0.08618207, 0.11556781, 0.09824824, 0.09599139],
 [0.09461512, 0.11862656, 0.18196459, 0.06744549, 0.13258033 ,0.10877688,
  0.08164507, 0.10988327, 0.10569704, 0.08124346, 0.09167752],
 [0.18489483, 0.15979382, 0.14886004, 0.11229113, 0.06408984 ,0.10878188,
  0.10408247, 0.13971456, 0.08008743, 0.08708248, 0.08107849],
 [0.1143987 , 0.14178765, 0.11504332, 0.09409295, 0.14846608 ,0.09164978,
  0.10531808, 0.1236298 , 0.09085797, 0.10353408, 0.09572679],
 [0.09134823, 0.18333428, 0.06302505, 0.0563465 , 0.06906034 ,0.11217101,
  0.07688379, 0.13060457, 0.07209561, 0.1487084 , 0.06914419],
 [0.09640865, 0.14902996, 0.16578074, 0.13939536, 0.10899882 ,0.14014123,
  0.05664185, 0.11880307, 0.07519414, 0.12987896, 0.11810896],
 [0.07099213, 0.1417898 , 0.14467969, 0.11238229, 0.11648406 ,0.12822886,
  0.07737696, 0.10963533, 0.09322052, 0.10890929, 0.11686232],
 [0.13554215, 0.17294644, 0.13922992, 0.12371149, 0.13147329 ,0.12837318,
  0.05721838, 0.15584772, 0.06825151, 0.12220958, 0.12268616],
 [0.09300659, 0.11913237, 0.15951261, 0.12304396, 0.08972759 ,0.10562398,
  0.10317242, 0.09868462, 0.08955632, 0.09398234, 0.11413589],
 [0.17582075, 0.16289668, 0.13008268, 0.13037091, 0.08922285 ,0.16882388,
  0.10636686, 0.1280454 , 0.09646773, 0.11326439, 0.10854864],
 [0.11357029, 0.11578237, 0.08397007, 0.0854061 , 0.0585152  ,0.1371105,
  0.1015774 , 0.105032  , 0.09698301, 0.09036818, 0.12406199],
 [0.12845116, 0.0868213 , 0.16666283, 0.07353416, 0.09300514 ,0.15800804,
  0.07605815, 0.09891659, 0.1012792 , 0.11866745, 0.10701899],
 [0.15656899, 0.10683422, 0.14790647, 0.16614269, 0.09092789 ,0.12198165,
  0.10508413, 0.07840032, 0.11997974, 0.09012214, 0.12639364],
 [0.18049499, 0.09308159, 0.09601595, 0.08670075, 0.1380677  ,0.10996287,
  0.10119987, 0.15389109, 0.08134082, 0.15560134, 0.10379282],
 [0.1366392 , 0.06861182, 0.12830151, 0.10548739, 0.10430815 ,0.1244036,
  0.14109647, 0.1008445 , 0.11905431, 0.11694147, 0.09626243],
 [0.15146581, 0.14932031, 0.15259417, 0.13645621, 0.09602339 ,0.12355068,
  0.0641019 , 0.12025768, 0.08825605, 0.11030188, 0.09656226],
 [0.19393997, 0.13886954, 0.06994536, 0.18106296, 0.08817119 ,0.09120451,
  0.10228209, 0.12222306, 0.12116821, 0.12464736, 0.10730805],
 [0.11696813, 0.17494462, 0.10983387, 0.05462454, 0.11445385 ,0.10903321,
  0.10978431, 0.11811305, 0.12615335, 0.11854328, 0.14573155],
 [0.16117079, 0.08819503, 0.07904793, 0.17900227, 0.10803966 ,0.07515911,
  0.16112653, 0.10687734, 0.12913785, 0.11841072, 0.10883801],
 [0.12351381, 0.1705136 , 0.20306543, 0.09954063, 0.08486122 ,0.11315741,
  0.09098593, 0.11689139, 0.09411653, 0.08634782, 0.13340668]])


X=np.repeat(np.arange(0.0,1.1,0.1),25)
y=list([row for row in matrix])
Y=[item for sublist in y for item in sublist]

# Plot heatmap
plt.figure()
plt.hist2d(X, Y)
plt.xlabel('$eta$')
plt.ylabel('Final aggregation')
plt.colorbar()
plt.tight_layout()
plt.show()