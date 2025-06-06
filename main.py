from weasyprint import HTML

# Load the updated HTML content into a string (adjusted with clubs section + resume.md changes)
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Shivam Pathak Resume</title>
  <style>
    @page {
      size: A4;
      margin: 0.5in;
    }
    body {
      font-family: 'Times New Roman', serif;
      font-size: 10pt;
      line-height: 1.15;
      margin: 0.5in;
    }
    h1 {
      font-size: 16pt;
      margin: 0;
    }
    h2 {
      font-size: 11pt;
      text-transform: uppercase;
      margin-top: 0.6em;
      margin-bottom: 0.2em;
      border-bottom: 1px solid #000;
    }
    p, li {
      margin: 0.1em 0;
    }
    ul {
      margin: 0;
      padding-left: 1em;
    }
    .section {
      margin-bottom: 0.3em;
    }
    .contact, .links {
      margin: 0;
    }
    .bold { font-weight: bold; }
  </style>
</head>
<body>
  <h1>Shivam Pathak</h1>
  <p class="contact">Denver, CO | 720-560-2050 | pathakshivam332@gmail.com</p>
  <p class="links">linkedin.com/in/shivampathak4568 | github.com/2h1vam12</p>

  <div class="section">
    <h2>Summary of Qualifications</h2>
    <ul>
      <li>Enthusiastic Computer Science student with practical experience in software development, database management, and leadership roles.</li>
      <li>Proven ability to optimize workflows, deliver impactful solutions, and contribute to organizational success.</li>
      <li>Seeking opportunities to further hone my technical expertise and leadership skills.</li>
    </ul>
  </div>

  <div class="section">
    <h2>Technical Skills & Projects</h2>
    <p><span class="bold">Programming:</span> C++, Python, Assembly, PHP, HTML</p>
    <p><span class="bold">Cyber-Security:</span> SQL Injection Testing, Secure Database Design</p>
    <p><span class="bold">Databases:</span> MySQL, PostgreSQL, Microsoft Power BI</p>
    <ul>
      <li>Zookeeper DBMS with security practices – Dec 2024 (SQL, PHP, HTML)</li>
      <li>UFC DBMS project – Dec 2024 (SQL, PHP, HTML)</li>
      <li>Scientific Calculator in Assembly – Dec 2024 (MASM)</li>
      <li>Stock Management System – Aug 2024 (C++)</li>
      <li>SQL Injection Attack Simulator – TBD (SQL, Python, HTML, C++)</li>
    </ul>
  </div>

  <div class="section">
    <h2>Education</h2>
    <p><span class="bold">University of Colorado Denver</span> — Denver, CO</p>
    <p>B.S. Computer Science | GPA: 3.5 | Expected: May 2026</p>
    <p>Minors: Business Fundamentals, Data Science | Certificate: Cybersecurity & Secure Computing</p>
    <p><span class="bold">Courses:</span> Assembly, OOP, DB Systems, Numerical Analysis, Algorithms, Networks, Architecture</p>
  </div>

  <div class="section">
    <h2>Professional Experience</h2>
    <p><span class="bold">Visa Inc.</span> — Systems Engineer Intern | May 2025 – Aug 2025</p>
    <ul>
      <li>Support enterprise infrastructure and automation development.</li>
      <li>Document internal systems and optimize technical workflows.</li>
      <li>Work on orchestration team using GenAI and internal APIs to automate tasks.</li>
    </ul>

    <p><span class="bold">IBM Z</span> — Student Ambassador | Feb 2025 – Present</p>
    <ul>
      <li>Organized events and promoted IBM Z technology across campus.</li>
      <li>Earned IBM Z badges and established student-led mainframe club.</li>
    </ul>

    <p><span class="bold">Society of Asian Scientists and Engineers</span> — Co-President | Dec 2024 – Present</p>
    <ul>
      <li>Led strategic outreach and secured sponsorship for inclusive STEM initiatives.</li>
      <li>Planned and executed professional development and networking events.</li>
    </ul>

    <p><span class="bold">Raising Cane’s</span> — Restaurant Manager | Mar 2021 – May 2025</p>
    <ul>
      <li>Managed marketing, training, and staffing operations for 20–30 crew per shift.</li>
    </ul>

    <p><span class="bold">D-Incuvator</span> — VP of Operations | Feb 2023 – Present</p>
    <ul>
      <li>Directed workshops and academic startup initiatives with NVIDIA support.</li>
      <li>Managed $20K+ in tech resources and a 15-member operations team.</li>
    </ul>

    <p><span class="bold">City of Arvada IT</span> — Data Analyst Intern | May 2020 – Oct 2020</p>
    <ul>
      <li>Built dashboards and data tools for local government stakeholders.</li>
    </ul>
  </div>

  <div class="section">
    <h2>Clubs & Volunteering</h2>
    <p><span class="bold">AI Student Association</span> — Member | Feb 2025 – Present</p>
    <ul>
      <li>Assisted with AI event planning and technical workshop development.</li>
    </ul>
    <p><span class="bold">Asian Student Society</span> — Member | Apr 2025 – Present</p>
    <ul>
      <li>Supported event operations and helped organize the Blossom Ball 2025.</li>
    </ul>
  </div>

  <div class="section">
    <h2>Certificates</h2>
    <ul>
      <li>IBM Z Xplore Concepts – Feb 2025 (IBM)</li>
      <li>IBM Z Xplore Advanced – Mar 2025 (IBM)</li>
      <li>IBM Z Day AI & Data Special Edition – Apr 2025 (IBM)</li>
      <li>Quantum Computing Foundations – May 2025 (Interskill)</li>
      <li>AI Anomaly Detection – Nov 2023 (NVIDIA)</li>
      <li>Transformer NLP Workshop – Aug 2024 (NVIDIA)</li>
      <li>Workplace Readiness – Jul 2021 (Red Rocks Community College)</li>
    </ul>
  </div>
</body>
</html>
"""

# Convert to PDF
output_path = "/mnt/data/Shivam_Pathak_Resume_2025.pdf"
HTML(string=html_content).write_pdf(output_path)

output_path
