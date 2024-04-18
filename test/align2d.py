from modeller import *

env = Environ()
aln = Alignment(env)
mdl = Model(env, file='2f9v', model_segment=('FIRST:A','LAST:A'))
aln.append_model(mdl, align_codes='2f9vA', atom_files='2f9v.pdb')

# Use the full path to open the file protease.ali
aln.append(file='protease.ali', align_codes='protease')

aln.align2d(max_gap_length=50)
aln.write(file='protease-2f9vA.ali', alignment_format='PIR')
aln.write(file='protease-2f9vA.pap', alignment_format='PAP')
