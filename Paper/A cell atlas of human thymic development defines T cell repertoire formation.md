[Park JE, Botting RA, Domínguez Conde C, Popescu DM, Lavaert M, Kunz DJ, Goh I, Stephenson E, Ragazzini R, Tuck E, Wilbrey-Clark A, Roberts K, Kedlian VR, Ferdinand JR, He X, Webb S, Maunder D, Vandamme N, Mahbubani KT, Polanski K, Mamanova L, Bolt L, Crossland D, de Rita F, Fuller A, Filby A, Reynolds G, Dixon D, Saeb-Parsy K, Lisgo S, Henderson D, Vento-Tormo R, Bayraktar OA, Barker RA, Meyer KB, Saeys Y, Bonfanti P, Behjati S, Clatworthy MR, Taghon T, Haniffa M, Teichmann SA. A cell atlas of human thymic development defines T cell repertoire formation. Science. 2020 Feb 21;367(6480):eaay3224. doi: 10.1126/science.aay3224. PMID: 32079746; PMCID: PMC7611066.](https://www.science.org/doi/10.1126/science.aay3224)
# 사전지식
### [[Thymus]]

### [[Cell Atlas]]

### [[Immune Repertoire]]
### [[V(D)J Recombination]]
### [[Beta-Selection]]
### [[Cell State]]
### [[Cell trajectory]]

### [[smFISH]]

---
# Cellular composition of the human thymus across life

<img src="https://www.science.org/cms/10.1126/science.aay3224/asset/9f6e7522-f159-4f30-928f-21b6fc4b3a9f/assets/graphic/367_aay3224_f1.jpeg">
Fig. 1 Cellular composition of the human thymus across life
- (A) 논문의 개요
- (B) 샘플들의 나이대, 장기(동그라미는 흉선, 네모는 간 혹은 그외), 색깔은 10x Genomics 화학품 종류
- (C) 흉선 유래 세포구성에 대하여 cell type에 따라 분류한 UAMP 시각화 자료
- (D) 나이대에 따른 UAMP 시각화 자료
- (E) 흉선 기질상(Thymix stromal) cell type에 따른 marker gene 발현 자료
- (F) 흉선 슬라이드에 대한 RNA smFISH
- (G) 나이대에 따른 cell type 분포

샘플에서 single cell들을 분리한 뒤, single cell들을 CD45, CD3 혹은 상피세포접착분자(epitherlial cell adhesion molecule, EpCAM)에 여부에 따라서 분류하였다. 이후 single cell transcriptome 분석을 TCRαβ profiling과 결합하여 수행하였다.

Doublet 제거 이후 남은 세포는 태아흉선유래 138,397개, 나머지 샘플들의 흉선유래 117,504개였다.

해당 샘플들에 대하여 **BBKNN 방법**을 통해 batch correction을 수행하였다.

이렇게 분류한 cell cluster는 40여가지가 넘게 나뉘었고 굵직하게 잡아서 42가지였다. (Fig1.C)

분류기준은 세포의 종류 혹은 세포의 상태에 따른 분류였다.

데이터를 통하여 T cell들이 다양한 형태의 세포로 분화되어 있음을 확인하였다.

**T cell의 종류 (분화)**
- Double Negative(DN)|
- Double Positive(DP)
- CD4<sup>+</sup> single positive
- CD8<sup>+</sup> single positive
- FOXP3<sup>+</sup> regulatory(T<sub>reg</sub>)
- CD8αα<sup>+</sup>
- γδ T cells

데이터에서는 T cell 외에도 B cells, NK cells, innate lymphoid cells(ILCs), macrophages, monocytes, DCs이 발견되었다. 또한 면역세포 외에 흉선의 미세환경(microenvironment)를 구성하는 세포들도 발견되었다.

**흉선의 미세환경 구성 세포 종류**
- TECs
- fibroblasts
- vascular smooth muscle cells (VSMCs)
- endothelial cells
- lymphatic endothelial cells

흉선의 fibroblast는 type1(Fb1)과 type2(Fb2) 종류로 세분화되어있었다.

|흉선의 Fb1|Fb2|
|:-|:-|
|<p>COLEC11 유전자를 발현하여 1차면역반응에 중요한 역할</p> <p>ALDG1A2 효소를 만들어 retinoic acid 생산을 통한상피성 성장(epithelial growth)을 조절</p>|<p>extracellular matrix (ECM) 유전자와 semaphorin 단백질을 통한 혈관발달 조절</p>|
| 흉선의 소염부위(perilobular)에 많이 분포 | 흉선의 소엽부위(interlobular)에 많이 분포 |

TEC 세포의 부분집단(subpopulation)도 확인하였다. TEC 세포의 부분집단으로는 수질흉선상피세포(medullary TECs, mTECs)와 피질흉선상피세포(cortical TECS, cTECs)가 확인되었다. 여러 나이대의 샘플에서 EpCAM-positive cells을 확인하여 더 많은 TECs를 확인하고자 했다.

그 결과 다른 종(아마도 쥐)에서도 발견되는 TEC 유전자들(TEC populations across species)이 인간에서도 발견되었다. 특히 여러 나이대의 샘플을 비교하였을 때, cTECs 유전자의 발현량이 임신 7~8주 때 많았고, mcTECs 유전자는 출산 직후까지 가장 많았다. 

주로 쥐의 흉선에서 발견되는 mTEC(IV)s를 발견할 수 있었다. mTEC(IV)s의 마커 유전자인 DCLK1이나 POU2F3는 량은 충분(enriched)했지만 이번 연구의 샘플에서는 특정하기 어려웠다 (but not specific to this population in human).

두 종류의 EpCAM<sup>+</sup> cell 타입이 인간샘플에서 특이적으로 나타났다.
- TEC(myo)s
- TEC(neuro)s

자가면역질환과 관련된 것으로 알려진 CHRNA1 유전자의 발현이 TEC(myo)s와 TEC(neuro)s, 그리고 mTEC(II)s에서 확인되었다.** 이를 통해 자가면역 중증 근무력증(myasthenia gravis) 치료를 위한 면역관용유도(tolerance induction)에 사용할 수 있는 세포 후보군을 넓힐 수 있다.**

## Coordinated development of thymic stroma and T cells

나이대에 따른 흉선세포의 변화를 살펴보았다.

임신 7~8주에는 림프구역에서 NK 세포, γδ T세포, ILC3s 세포가 주로 발견되었고, 일부에서 αβ T세포로 분화됨이 발견되었다. T cell의 분화는 주로 임신 7주의 DN기(double negative stage; CD4와 CD8이 둘 다 없는 T cell 단계)에서 관찰되었다. 이후 12주까지 성장하면서 SP(single positive)단계와 동일해졌다. 역으로 초기 림프구의 량은 감소하였다.


성인에서는 흉선이 퇴화된다는 것이 형태적으로 확인되었다. 

해당 성인 흉선샘플들은 지라(spleen)샘플, 림프관샘플들과 함께 채취되었다. 이에 따라 실험 자원자 개개인마다 3가지 장기에서 가져온 샘플들을 비교할 수 있었다. 이를 통해 분화가 끝난 T 세포가 지라와 림프관 뿐 아니라 흉선에서도 발견됨을 확인하였다.

이 말은 즉 해당 T 세포들이 흉선 밖에서 분화 및 성숙된 다음에, 다시 흉선으로 들어갔거나 혹은 순환중인 세포(circulating cells)에 의하여 오염되었을 수 있음을 시사한다. 특히 CD4+ T 림프구(CD4+ CTLs)가 퇴화 중인 흉선 내에서 많이 발견되었다. 또한, 기억 T세포와 기억 B세포가 많이 발견된 샘플도 있었다.

연구팀은 흉선상피세포와 성숙한 T 세포 사이의 상호작용이 존재하며, T 세포의 성숙 및 분화(mutual differentiation)에 영향을 준다는 것을 확인하였다. 이를 "thymic cross-talk"라고 한다.

Fibroblast의 경우 어릴 때는 Fb1의 량이 많다가 시간이 지남에 따라 Fb1과 Fb2 량이 같아졌다. 동시에 순환세포(cycling cells)의 량은 감소했다. 이 사실은 흉선의 fibroblast에 대한 체외배양(explant culture) 및 fluorescence-activated cell sorter(FACS) 분석을 통하여 동일하게 확인된 내용이다.

마지막으로 면역세포의 조성 또한 임신 중 및 생후 기간에 따라 큰 차이를 보였다. Macrophage는 임신 초기에 많았으며, DCs는 이후 발전에 따라 양이 증가하였다. DC1의 경우 착상 12주 후부터 양이 많았으며, pDCs의 경우 생후에 양이 증가하였다.

CellPhoneDB.org의 데이터들을 활용하여 세포간의 상호작용(cellular interactions)를 조사함으로써, 흉선 기질(thymic stroma)과 T 세포의 성장을 조절하는 요소를 살펴봤다. 이를 통해 세포 사이에서 특이적으로 발현하는 ligand-receptor를 예측하였다.

세포간의 상호작용을 예측하는 과정에서, 흉선의 발달과 관련된 신호들이 서로 다른 세포종류와 성장단계에서 발현된다는 사실을 관측하였다. Lymphtoxin signalling(LTB:LTBR)과 같은 신호가 여러 면역세포에서 발현하였고, 이 신호는 대부분의 기질 세포에서 받아들여졌다.

## Conventional T cell differentiation trajectory

<img src="https://www.science.org/cms/10.1126/science.aay3224/asset/fce4473d-ba5b-4723-b40b-4f2581cc5181/assets/graphic/367_aay3224_f2.jpeg">

태아의 간은 주요한 조혈기관(hematopoietic organ; 혈액을 만드는 기관)이며, 조혈모세포(hematopoietic stem cells)와 multipotent progenitors(다능전구세포; HSCs, MPPs 포함)가 만들어지기 시작하는 공간(source)이다.

연구팀은 동일한 태아에서 채취한 흉선과 간 샘플을 동시에 분석하였다. 해당 데이터들을 통합하여 간 HSCs, 간 MPPs, 초기 흉선 전구세포(early thymic progenitors, ETPs), DN기 흉선세포를 각각 조사하였다. (Fig. 2 (A), (B), Fig. s12)

This positioned thymic ETPs at the isthmus between fetal liver HSCs/MPPs and pre/pro-B cells. We integrated our liver/thymic hematopoietic progenitor subset with the single-cell transcriptomes of human hemato- poietic progenitors sorted from bone marrow using defined markers (Fig. S13)

분석결과를 통하여 태아의 간 내에서 ETPs의 위치가 척수에서 유래의 다림프성 전구세포(multi-lymphoid progenitor, MLP) 옆이나 초기 림프성 전구세포(early lymphoid progenitor) 옆이라는 사실을 밝혀냈다.

T cell 분화의 이후과정(downstream)을 알아보기로 위하여 T cell이 분화하는 과정을 시각화하였다. (Fig. 2C, Fig. S14A, data S1)

해당 umap 그래프를 통하여 T cell 분화의 과정을 알 수 있다. 이 분화과정을 검증하기 위하여 (to confirm the validity of this trajectory), T cell 분화를 확인할 수 있는 hallmark 유전자를 덮어 씌워서 그래프를 그려봤다. 흉선에서는 CD4, CD8A, CD8B 유전자의 위치를 통해 데이터를 검증했으며, 세포주기는 CDK1 유전자, 재조합은 RAG1 유전자를 통해 검증했다. 그리고 전체 재조합 유전자로 TCRα, TCRβ를 활용했다. (Fig. 2D~F)

Fig. 2D의 그래프를 통하여 세포발달이 DN세포(CD4, CD8 negative)에서 시작하였음을 알 수 있다. 해당 세포는 CD4와 CD8을 동시에 나타내며 DP세포(CD4, CD8 positive)가 되고, 이후 $\scriptstyle CCR9^{high}T\alpha\beta$에 들어가서 분화가 시작되어, 결국 SP세포(CD4 혹은 CD8 둘 중 하나만 positive)로 성숙하게 된다.

또한, Fig. 2C 그래프에서 회색으로 세포종류를 확인했는데, 이 부분은 DN-DP 중간(junction)에서 $\scriptstyle \gamma\delta$ T세포로 분화되는 부분으로 보인다.

Fig. 2E를 보면 T cell의 분화과정에 있어서 발현하는 유전자의 종류는 크게 두 가지로 보인다.

Fig. 2C를 보면 각 주기 옆에 (P) 혹은 (Q)로 표시해놨다. 이는 세포들 중에서 증식(proliferating)중인 세포군과 증식을 멈춘 휴지기(quiescent)의 세포군으로 나눠놓은 것이다. RAG1, RAG2 같은 VDJ 재조합 유전자는 (P)시기 말기에 증가하기 시작하여 (Q)시기에 정점을 찍는 것이 보인다. 따라서 재조합이 일어나기 전에 증식이 발달한다는 것을 반영하고 있다.

Fig. 2F를 통하여 TCR에 대한 유전자 재조합 데이터를 살펴보았다. DN기의 흉선세포에서는 재조합된 TCRβ 서열이 증식(P)말기에서 많이 발견되었다. 동시에 해당 시기에는 pre-TCRα(PTCRA) 유전자의 재조합에서 발견되는 특징들과 발현이 많이 나타났다.

V(D)J 유전자 재조합 결과 heavy chain을 구성할 수 있는 경우 'productive recombination event'라고 하며, 만약 heavy chain을 구성할 수 없고 항체를 생성할 수 없는 경우를 'non-productive recombination event)라고 한다.

Fig. 2H를 통하여 V(D)J 유전자 재조합에 실패하여 항체를 구성할 수 없는 세포의 비율인 non-productive chain ratio를 살펴보았을 때, TCRβ 중 DN기의 세포에서 상대적으로 높았다. 이후 DP기에 들어가면 non-productive TCRβ 발현 비율이 줄어들었는데, β-selection 과정을 잘 반영한 것이라고 할 수있다.

특이한 점으로 TCRβ 중에서 non-productive recombination의 비율이 가장 높았던 때는 DN(Q)였다. 이는 즉 세포가 TCRβ에서 한 쪽 allele에 대해서 성공적으로 재조합을 한 다음에 다른 쪽 allele를 재조합하던 도중 안정성을 잃어버렸음을 의미한다(?) DP기에는 TCRα chain이 DP(P)에서 가장 높게 발견되었다. TCRβ와 다르게 non-productive TCRα은 DP(Q)에서 줄어들었다.

이 논문의 '전사체에 의거한 clustering' 데이터와 인터넷에 공개되어있는 '단백질 마커에 기반한 sorting strategy' 데이터를 맞춰보기 위하여, 인터넷에 있는 데이터 중 '마이크로어레이로 분석한 FACS-sorted thymocytes' 데이터를 골랐다. (Fig. S16)

On the basis of cell cycle gene signature and marker gene expression, DN(P), DN(Q), and DP(P) stages are closely matched to CD34$^{+}$CD1A$^{+}$,ISP CD4$^{+}$,and DP CD3$^{-}$ populations, respectively.

DP(Q)기와 Tαβ(entry)기의 세포들이 보이는 특징들이 마이크로어레이 데이터 중에서 DP CD3$^{+}$기의 데이터와 상응하였다. β-selection 이전 단계의 데이터를 비교하였을 때, DN(Q) 세포의 데이터가 ISP CD4$^{+}$세포 데이터와 상응하였다. 이는 해당 세포가 β-selection의 체크포인트임을 의미한다(Fig. 2F, Fig. S15)


Conventional T cells(αβ형)의 발달 과정을 모델링하기 위하여, 잘 알려진 유전자와 전사체 factors를 가지고 이들과 일치하는 세포들에 대해 pseudo time 분석을 시행하였다. (Fig. 2G) 추가적으로 T cell 성장과 관련된 마커들을 살펴보았다 (초기 DN기의 ST18 유전자, DP기의 AQP3 유전자, DP에서 SP로 넘어가는 시기의 TOX2 유전자). 해당 유전자들을 포함하여 각 발달단계와 유전자의 상관관계를 그래프로 표현하였다. (Fig. 2I)
## Development of T$\scriptstyle regs$ and unconventional T cells

<img src="https://www.science.org/cms/10.1126/science.aay3224/asset/7cb4b934-9e67-4566-a088-0779a7f49007/assets/graphic/367_aay3224_f3.jpeg">

Unconventional T cell 마커 유전자의 발현을 추적하여, 다양한 unconventional T cell 타입을 알아낼 수 있었다. (Fig. 2I, Fig. 3(A)(B))

Unconventional T cell의 경우 성장을 위해 경쟁선택(agonist selection)이 필요한 것으로 보고되었으며, 실제로 unconventional T cell 데이터에서 TCR chain 구성에 실패한 세포의 비율이 적었다.

In support of this, we observed a lower ratio of nonproductive TCR chains for these cells, implying that they reside longer in the thymus than do conventional T cells (Fig. 3C).

수정 후 10주가 지나면 태아의 흉선은 성숙해지게 된다. 성숙해진 흉선에서 unconventional T cell이 계속 축적된다고 가정했을 때, unconventional T cell의 성장이 흉선의 의존적으로 진행된다는 점을 확인할 수 있다고 가정했다. 데이터를 통해 확인한 결과 unconventional T cell (γδT, NKT, T$\scriptstyle regs$...)가 흉선에서 많음을 확인했고, 이 세포들은 흉선 유래임을 확인했다.

Unconventional T cell의 대부분은 T$\scriptstyle regs$ 세포가 차지했다. 특히 T$\scriptstyle regs$와 αβ T세포 사이에 유의미한 분화과정(clear differentiation trajectory)을 확인하였고, 이를 T$\scriptstyle regs(diff)$라고 이름 붙였다.

T$\scriptstyle regs(diff)$의 경우 일반적인 T$\scriptstyle regs$와 관련된 유전자들을 발현하였는데, FOXP3, CTLA4 유전자는 적게 발현했지만 IKZF4, GNG8, PTGIR 유전자는 높게 발현했다. 이 유전자들은 T$\scriptstyle regs$ 뿐만 아니라 자가면역질환과도 연관이 있다.

연구팀은 T$\scriptstyle regs$ 중에서도 T$\scriptstyle regs$와는 연관이 없는 세포군은 발견했다. 이 세포군들은 noncoding RNA, MIR155HG 유전자를 발현했다. 이에 따라 해당 세포군은 T$\scriptstyle (agonist)$라고 이름을 붙였다. (Fig. 3 (A),(B))

T$\scriptstyle (agonist)$의 특이하게 IL2RA 단백질을 만들어내지만 정작 FOXP3 mRNA 발현량은 적었다. 이러한 특징은 쥐 모델에서 발견된 CD25$^+$FOXP3$^-$T$\scriptstyle reg$ 전구체와 유사하다. (Fig. S17)

참고문헌 52번의 내용에 기반하여 살펴본 바, T$\scriptstyle reg$의 전구체 CD25$^+$와 FOXP3$^{1o}T\scriptstyle reg$를 보았을 때, 둘 다 연구팀이 이름 붙였던 세포군 T$\scriptstyle (agonist)$, T$\scriptstyle regs(diff)$에서 발현량이 높은 것으로 나타났다. (Fig. S17)

또한, T$\scriptstyle (agonist)$, T$\scriptstyle regs(diff)$ 세포군 모두 성숙한 T$\scriptstyle regs$ 와 연관이 있는 것으로 나타났으며, T$\scriptstyle regs$ 의 전구체는 흉선에 존재하는 두 종류의 세포임을 시사했다.

Fig. 3 (B)를 통하여 기타 다른 unconventional T cell을 확인할 수 있다. 해당 세포들은 CD8αα$^{{+}}$T세포, NKT-like 세포, T$\scriptscriptstyle H$17-like 세포였다.

CD8αα$^{{+}}$T 세포의 경우 다시 세가지 세포군으로 구별할 수 있었다. (Fig. 3 (E))

-   GNG4$^+$CD8αα$^{{+}}$T(i) 세포
-   ZNF683$^+$CD8αα$^{{+}}$T(ii) 세포
-   CD8αα$^{{+}}$ NKT-like 세포 중 Eomesodermin (Eomes) T-box transcription factor로 마킹된 것

GNG4$^+$CD8αα$^{{+}}$T(i) 세포와 ZNF683$^+$CD8αα$^{{+}}$T(ii) 세포는 초기에는 PDCD1을 발현한다는 공통점을 가진다. (이 발현은 분화과정에서 줄어든다. Fig. S14 (B))

GNG4$^+$CD8αα$^{{+}}$T(i) 의 경우 후기 DP기에 뚜렷하게 발생경로를 보여주지만, ZNF683$^+$CD8αα$^{{+}}$T(ii)는 그렇지 못하고 알파베타감마델타 T 세포 신호가 섞여있으며, GNG4$^+$CD8αα$^{{+}}$T(i) 세포와 감마델타 T 세포 사이에 있다.