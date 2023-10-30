Single-molecule Fluorescene in situ Hybridization.

- 유전자의 발현 정도는 mRNA level을 기준으로 측정되었으며, smFISH 기술은 그 한 종류이다.
# 등장배경
- smFISH 이전에는 reverse transcription-PCR(RT-PCR), Northern blot, RNA-seq 등의 방법을 통하여 mRNA level을 측정했다.
- 그러나 위의 방법들은 다수의 세포에서 구별없이 RNA를 추출하는 방식이었기 때문에, 각 세포마다의 유전자 발현량은 알 수 없었다.
- 따라서 **RNA가 정확하게 어느 세포에서 유래했는지**, 즉 RNA와 세포의 위상(the spatial distribution)을 알기위한 연구가 이어졌으며, 그 결과 smFISH가 개발되었다.
# 특징
- smFISH는 DNA oligonucleotide가 달려있는 probe와 세포들을 결합시키는 방법이다.
- 각 DNA oligonucleotide 말단에는 형광표지가 되어있어 추적이 가능하다.
- 먼저 RNA 분자 하나에 여러 개의 probe가 붙은 형태를 만든다.
- 그리고 probe에 의해서 signal-to-noise 비율이 올라가면, 현미경을 통해 관찰이 가능하게 된다.
- 3D 가우시안 피팁 알고리즘(Gaussian fitting algorithm)을 통하여 이미지 상의 형광빛들을 분석할 수 있다.
# 장점
- smFISH는 RNA 분자 각각의 수준까지 구별할 수 있는 해상도와, 세포 내의 RNA 분자의 위상(spatial information)을 알 수 있는 장점을 가진다.
# 단점
- smFISH의 단점으로는 세포가 고정되어있어야 하므로 **살아있는 세포 내에서 RNA의 변화를 관찰할 수 없으며**, 형광빛을 1~4개만 사용할 수 있으므로 한번의 실험에서 1~4개의 유전자만 분석할 수 있다는 단점이 있다.
# 참고
- https://bio-protocol.org/e3070