CREATE TABLE public.vaccination_coverage (
    vaccine character varying(256) ENCODE lzo,
    dose character varying(256) ENCODE lzo,
    geography character varying(256) ENCODE lzo,
    geography_type character varying(256) ENCODE lzo,
    year_season character varying(256) ENCODE lzo,
    dimension character varying(256) ENCODE lzo,
    dimension_type character varying(256) ENCODE lzo,
    coverage_estimate double precision ENCODE raw,
    _95_ci character varying(256) ENCODE raw,
    population_sample_size double precision ENCODE raw,
    coverage_estimate_log double precision ENCODE raw,
    coverage_rate double precision ENCODE raw
) DISTSTYLE AUTO;