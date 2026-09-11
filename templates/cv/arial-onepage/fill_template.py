"""Fill a template.docx's [TOKENS] and write a new .docx.

This is the same mechanic MASTER-RESUME-REFERENCE.md mandates: unpack, edit the
text runs in word/document.xml, repack. It never rebuilds the file, so the
approved Arial formatting survives untouched.
"""
import zipfile, sys, os, html

def fill(src, dst, values):
    zin = zipfile.ZipFile(src)
    doc = zin.read('word/document.xml').decode('utf-8')
    missing = []
    for token, val in values.items():
        t = f'[{token}]'
        if t not in doc:
            missing.append(token)
        doc = doc.replace(t, html.escape(val, quote=False))
    if os.path.exists(dst):
        os.remove(dst)
    zout = zipfile.ZipFile(dst, 'w', zipfile.ZIP_DEFLATED)
    for item in zin.infolist():
        data = zin.read(item.filename)
        if item.filename == 'word/document.xml':
            data = doc.encode('utf-8')
        zout.writestr(item, data)
    zout.close()
    zin.close()
    # report tokens still unfilled
    left = [w.split(']')[0] for w in doc.split('[')[1:] if ']' in w]
    return missing, sorted(set(left))


DUMMY = {
    'YOUR_NAME': 'JORDAN RIVERA',
    'YOUR_EMAIL': 'jordan.rivera@example.com',
    'YOUR_PHONE': '555-010-3344',
    'YOUR_LINKEDIN_URL': 'linkedin.com/in/jordanrivera',
    'YOUR_LOCATION': 'Boston, MA',
    'PROFILE_STATEMENT': ('Product leader with 12 years in healthcare technology, building AI-powered '
                          'products across payer and provider workflows. Shipped machine learning systems '
                          'in production within HIPAA and SOC 2 environments. Led a platform rebuild that '
                          'doubled recurring revenue year over year. MBA, Healthcare Management.'),
    'COMPANY_1': 'Northwind Health', 'CITY_STATE_1': 'Boston, MA',
    'JOB_TITLE_1': 'Director of Product', 'DATES_1': '2021 - 2026',
    'COMPANY_2': 'Bluepeak Advisory', 'CITY_STATE_2': 'Boston, MA',
    'JOB_TITLE_2': 'Technical Advisor', 'DATES_2': '2024 - Present',
    'COMPANY_3': 'Metro General Hospital', 'CITY_STATE_3': 'Boston, MA',
    'JOB_TITLE_3': 'Technical Architect', 'DATES_3': '2017 - 2021',
    'COMPANY_4': 'Cedar Systems', 'CITY_STATE_4': 'Providence, RI',
    'JOB_TITLE_4': 'Application Consultant', 'DATES_4': '2015 - 2017',
    'COMPANY_5': 'Ridgeline Software', 'CITY_STATE_5': 'Atlanta, GA',
    'JOB_TITLE_5': 'Program Developer', 'DATES_5': '2013 - 2015',
    'INSTITUTION_1': 'State University', 'DEGREE_1': 'MBA, Healthcare Management',
    'EDU_LOCATION_1': 'Boston, MA', 'YEARS_1': '2020 - 2022',
    'INSTITUTION_2': 'Institute of Technology', 'DEGREE_2': 'BS, Biomedical Engineering',
    'EDU_LOCATION_2': 'Atlanta, GA', 'YEARS_2': '2009 - 2013',
    'LANGUAGES': 'English (native), Spanish (professional working proficiency)',
    'PRODUCT_AND_AI_SKILLS': 'AI Agents, OCR, Retrieval Prototyping, Roadmapping, PRDs, Experiment Design',
    'ENGINEERING_AND_ARCHITECTURE_SKILLS': 'Microservices, REST APIs, AWS, GCP, HIPAA/SOC 2, HL7, FHIR, CI/CD',
    'TECHNICAL_STACK': 'React.js, Node.js, Python, PostgreSQL, TypeScript',
    'DOMAIN_SYSTEMS': 'Epic, Cerner Millennium, Allscripts',
    'VOLUNTEER_LINE': 'Organized regional medical supply drives for community clinics.',
}
for r in range(1, 6):
    for b in range(1, 6):
        DUMMY[f'ROLE_{r}_BULLET_{b}_LEAD'] = f'Representative Achievement Heading {b}'
        DUMMY[f'ROLE_{r}_BULLET_{b}_TEXT'] = (
            'Delivered a measurable outcome against a named constraint, quantified with a concrete '
            'metric so the reader can judge scale and impact without further context.')

if __name__ == '__main__':
    missing, left = fill(sys.argv[1], sys.argv[2], DUMMY)
    print(f'tokens not found in template: {missing or "none"}')
    print(f'tokens left unfilled:         {left or "none"}')
