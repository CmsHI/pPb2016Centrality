import FWCore.ParameterSet.Config as cms

externalLHEProducer = cms.EDProducer("ExternalLHEProducer",
    args = cms.vstring('.','slightGridpack_ProdType6_Channel11_beam208.tgz','5020','6'),
    nEvents = cms.untracked.uint32(100000),
    numberOfParameters = cms.uint32(4),
    outputFile = cms.string('cmsgrid_final.lhe'),
    scriptName = cms.FileInPath('../runcmsgrid_starlight.sh')
)

generator = cms.EDFilter("Pythia8HadronizerFilter",
                         maxEventsToPrint = cms.untracked.int32(1),
                         pythiaPylistVerbosity = cms.untracked.int32(1),
                         filterEfficiency = cms.untracked.double(1.0),
                         pythiaHepMCVerbosity = cms.untracked.bool(False),
                         comEnergy = cms.double(5020.),
                         PythiaParameters = cms.PSet(
                                parameterSets = cms.vstring('skip_hadronization'),
                                skip_hadronization = cms.vstring('ProcessLevel:all = off',
                                        'Check:event = off')
                        )
)

ProductionFilterSequence = cms.Sequence(generator)
