from pyopenms import*
seq=AASequence.fromString("VAKA")
seq_wz_MonoWeight=seq.getMonoWeight()
seq_monoweight_2=seq.getMonoWeight(Residue.ResidueType.Full,2)
mz=seq.getMZ(2)
print(f"The Peptide {seq} With MonoWeight (Mass out H2O) > {seq_wz_MonoWeight}")
print(f"MonoWeight and H2 > {seq_monoweight_2} mz > {mz}")
resultOfAllMonoWeight=0
for i in seq:
    print(i.getName()+">"+str(i.getMonoWeight()))
    resultOfAllMonoWeight+=i.getMonoWeight()
print(f"VAKA = {resultOfAllMonoWeight}")
print(f"{bool(seq_monoweight_2==resultOfAllMonoWeight)}")