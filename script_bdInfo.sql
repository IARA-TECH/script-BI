CREATE TABLE abacus_survey (
    id SERIAL PRIMARY KEY,
    email VARCHAR(150) NOT NULL UNIQUE,
    age VARCHAR(15) NOT NULL,
    job_responsibilities TEXT NOT NULL,
    state VARCHAR(30) NOT NULL,
    abacus_counting_importance VARCHAR(25) NOT NULL,
    abacus_counting_time VARCHAR(40) NOT NULL,
	has_problems VARCHAR(3) NOT NULL,
    technology_acceptance INT,
    can_use_mobile VARCHAR(3),
    is_signal_quality_satisfactory VARCHAR(3),
    photo_without_interference VARCHAR(3),
    lighting_quality INT,
    would_use_or_recommend VARCHAR(3) NOT NULL
);

CREATE TABLE issues (
    id SERIAL PRIMARY KEY,
    survey_id INT REFERENCES abacus_survey(id) ON DELETE CASCADE,
    issue_description TEXT NOT NULL
);

ALTER TABLE issues
ADD CONSTRAINT unique_issue_per_survey UNIQUE (survey_id, issue_description);

ALTER TABLE abacus_survey
ADD COLUMN updated_at DATE NOT NULL DEFAULT current_date;