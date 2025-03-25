from numpy import ndarray
from visual.strategies.fft_strategy import FFTStrategy
from visual.strategies.time_domain_envelope_strategy import TimeDomainEnvelopeStrategy


class FFTSmoothStrategy(FFTStrategy):

    def __init__(self, chunk_size, envelop_strategy: TimeDomainEnvelopeStrategy):
        self.envelop_strategy = envelop_strategy
        super().__init__(chunk_size)

    def transform(self, data: ndarray):
        fft_transformation = super().transform(data)
        return self.envelop_strategy.transform(fft_transformation)
