from lib import *

example_plaintext_postings = [
(
    'React JS front-end developer - Systemates Inc',
    '''
    If you are a senior JavaScript developer with fantastic React.js experience we have an exciting project for you at a competitive salary.

    You will be working with senior level developers to create user interface components and implement them following well-known Reactjs workflows (such as Flux or Redux). You will ensure that these components and the overall application are robust and easy to maintain. You will coordinate with the team working on different layers of the infrastructure. Therefore, a commitment to collaborative problem solving, sophisticated design, and quality product is very important.

    Responsibilities

    Developing new user-facing features using React, Redux Toolkit.
    Building reusable components and front-end libraries for future use
    Translating designs and wireframes into high quality code
    Optimizing components for maximum performance across a vast array of web-capable devices and browsers
    Skills

    Minimum 3 years of solid React experience.
    Strong proficiency in JavaScript, including DOM manipulation and the JavaScript object model
    Thorough understanding of React.js and its core principles
    Experience with popular Reactjs workflows (such as Flux or Redux)
    Familiarity with newer specifications of EcmaScript
    Familiarity with RESTful APIs
    Familiarity with .Net Core a HUGE PLUS!
    Knowledge of modern authorization mechanisms, such as OAuth 2.0 Authorization Code Grant
    Familiarity with modern front-end build pipelines and tools
    Experience with common front-end development tools such as Babel, Webpack, NPM, etc.
    Ability to understand business requirements and translate them into technical requirements
    A knack for benchmarking and optimization
    '''
),
(
    'Cybersecurity Infrastructure Engineer',
    '''
    Minimum of 3 - 5 years’ experience in security in an enterprise environment
    Experience with platform security technologies, including but not limited to, security orchestration and response, attack surface management, IoT security, and email security
    Experience with network segmentation and/or security zones for applicable data protection according to data classification
    Working knowledge of information systems security standards and practices (e.g., access control, system hardening, system auditing, log file monitoring, security policies, and incident handling)
    Demonstrated experience of “hands on” security knowledge of one or more of the following platforms: Windows, Linux, AIX, iSeries
    Working knowledge of networking protocols, web technologies, and cloud computing
    Ability to interpret information security data and processes to identify potential compliance issues
    Ability to quickly understand complicated data flows in order to identify and validate security requirements
    A team player with the willingness to establish a strong positive working relationship with all areas of the business
    Ability to work effectively; independent of assistance or supervision
    Innovative, creative, and extremely responsive with a strong sense of urgency
    Ability to clearly communicate Information Security matters to executives, auditors, end users, and engineers using appropriate language, examples, and tone
    One or more professional network and security certifications, such as Security , Network , CCNA, GSEC, CISA or CISSP (or equivalent work experience)
    Experience performing computer forensics
    Familiarity ITILv2/v3 processes, such as Service Support, Service Delivery or Continual Service Improvement
    Familiarity with Regulatory Compliance and industry standards, such as HIPAA, SOX, and PCI
    Familiarity in a DevOps or DevSecOps environment
    If hired, you will be required to provide proof of authorization to work in the United States
    Responsibilities
    This Security Analyst position will be a member of the Cybersecurity Infrastructure - Platform Security team that will support, maintain, and develop tools and projects involving platform security technologies
    Additionally, they will work with management and suppliers for product consideration; perform auditing of information system activities; create and maintain documentation related to policies, standards, and procedures; and mentor team members
    This will involve working with many groups throughout IT both domestically and internationally
    Works analytically to solve both tactical and strategic problems
    Assesses centralized user and configuration management systems
    Performs and/or coordinates regular security assessments of existing or new infrastructure
    Analyzes network protocols, data flows, architectural diagrams, and/or network traffic flows in conjunction with security zones and/or architectural strategies to ensure secure communication of data
    Creates and maintains network and system diagrams and other documentation
    Performs duties necessary to assist in establishing practices and system configurations to ensure the safety of information systems’ assets and to protect information systems from intentional or inadvertent access or destruction
    Works with information systems custodians (i.e., department managers, user community, and systems administrators) at different levels in the organization to understand their respective security needs and assists with implementing practices and procedures consistent with Costco’s Information Security Policy
    Assists with auditing of information systems’ activities and systems to confirm information security policy compliance and provides management with security policy compliance assessments
    Partners with other Information Security groups to conduct security assessments on new solutions and systems, periodic security risk assessments on existing systems, and identifies and/or recommends appropriate security countermeasures and best practices
    Shares knowledge with co-workers and assists them in understanding technical and business topics
    '''
),
(
    'Nvidia Graphics Performance Intern',
    '''
    Qualifications
    Ability to model a positive tone and work ethic to junior members of the team
    Ability to provide and receive good feedback when iterating levels
    Bachelor’s degree or the equivalent in Interactive Entertainment or Animation and up to two years of experience in Design (Narrative, Cinematics, Level or Combat Design) and demonstrated ability in the following areas:
    Proven track record of building and shipping large level environments
    Strong eye towards aesthetics, with an ability to work hand-in-hand with art teams
    Excellent documentation, communication, interpersonal, and organizational skills
    Ability to maintain focus and self-motivation towards the current project goals
    Live near or be able to relocate to Frisco, Texas
    Have shipped a AAA title, with a preference towards Unreal technology and first person shooters
    Shipped games using Unreal 4 technology
    Experience with the certification and shipping process on modern consoles
    Experience working with large inter-disciplinary teams
    Co-op and/or Online Multiplayer experience
    Previous leadership experience
    Responsibilities
    This role involves working with the Lead Level Designer and Creative Director to pitch, build, polish, and ship levels using Unreal Engine 4
    Level Designers are responsible for owning the vision of their levels, and working with a variety of other departments to see that vision come to fruition
    It involves close collaborative work with artists, mission designers, writers, coders, and a variety of other disciplines to ensure the level ships on time at a high standard of quality, while also being fun and memorable to players
    Develop single player and cooperative levels based on existing game design documents, direction from project leadership, and collaboration with peers
    This involves taking a design all the way from a paper design to a shipping product, iterating over time based on feedback, creative goals, and project deadlines
    Prototype, iterate, and polish moment-to-moment gameplay while working with narrative designers, enemy designers, artists, and other disciplines to ensure quality combats and mission experiences for the final customers
    Mentorship and sharing of expertise with junior level designers and other design staff
    Should include videos or screenshots of shipped levels, and any additional documentation showing design and iteration process
    Understanding of modern level design practices, including layout, pacing, technical implementation, and above all else creating fun experiences for players
    '''
),
(
    'Graphics/Renering Game Engineer',
    '''
    5+ years experience, ideally within a Graphics/Rendering games capacity
    Expert knowledge of real time rendering
    Strong C++ knowledge and multi-threaded programming techniques; ability to code and architect various core engine systems
    Excellent knowledge of a broad range of graphics APIs and shader languages including DirectX and OpenGL/GLSL
    Experience with Current console game rendering
    Exposure to third-party tools like Houdini, Substance Painter, and Z-Brush in terms of how they can function in a graphics pipeline
    Develops core rendering features, engine components and tools
    Researches and implements cutting-edge rendering techniques
    Creates reusable & scalable rendering technologies
    Writes technical design specifications
    Designs, maintains, implements, tests and debugs code, pipelines and other rendering-related sub-components and packages
    Profiles and optimizes rendering modules of a game engine
    Stays up to date with latest hardware & software changes impacting the rendering domain
    '''
)
]

id_set = set()
for page in range(0, 100, 20):
    id_set.update(fetch_class_ids(page))

class_descriptions = {
    class_id: fetch_class_data(class_id)['description']
    for class_id
    in id_set
}

class_descriptions_encoded = {
    class_id: encode_text(description)
    for class_id, description
    in class_descriptions.items()
}

for post_position, posting_content in example_plaintext_postings:
    sorted_class_recommendations = compute_similarity(
        encode_text(posting_content),
        class_descriptions_encoded,
    )

    print(post_position)
    for rec in sorted_class_recommendations:
        print(fetch_class_data(rec[0])['title'], rec[1])
