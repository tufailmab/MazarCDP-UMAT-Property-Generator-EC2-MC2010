</head>
<body>
  <h1>Mazar Concrete Damage Model – UMAT Property Generator</h1>

  <p>
    This Python script computes the required 21 input parameters for the
    <strong>Mazar Concrete Damage Model</strong> UMAT subroutine used in finite element simulations. Calculations are based on <strong>Eurocode 2 (EC2)</strong> and <strong>Model Code 2010 (MC2010)</strong> to support accurate material modeling for concrete structures.
  </p>

<p>
  <strong>Cite this Tool:</strong>
  <a href="https://doi.org/10.5281/zenodo.21425212">
    <img src="https://zenodo.org/badge/DOI/10.5281/zenodo.21425212.svg" alt="DOI">
  </a>
</p>

  </p>

  <h2>Key Features</h2>
  <ul>
    <li><strong>Input:</strong> Concrete compressive strength (f<sub>ck</sub>) in MPa.</li>
    <li><strong>Output:</strong> 21 concrete parameters formatted as <code>props(1)</code> to <code>props(21)</code>.</li>
    <li><strong>Includes:</strong>
      <ul>
        <li>Elastic modulus (E)</li>
        <li>Poisson’s ratio (ν)</li>
        <li>Tensile strength (f<sub>ctm</sub>)</li>
        <li>Fracture energy (G<sub>FI<sub>t</sub></sub>, G<sub>FI<sub>c</sub></sub>)</li>
        <li>Strain limits (ε<sub>c1</sub>, ε<sub>cu1</sub>)</li>
      </ul>
    </li>
    <li><strong>Output Format:</strong> Excel file automatically saved to the working directory.</li>
  </ul>

  <h2>Usage</h2>
  <ol>
    <li>Run the script:
      <pre><code>python Mazar_ConcreteModel_UMAT_Props.py</code></pre>
    </li>
    <li>Enter the desired concrete compressive strength (MPa) when prompted.</li>
    <li>Excel file will be saved in the current folder.</li>
  </ol>

  <h2>Requirements</h2>
  <ul>
    <li>Python 3.x</li>
    <li>Libraries: <code>math</code>, <code>pandas</code>, <code>os</code></li>
  </ul>

 <h2>Developer Information</h2>
  <ul>
    <li><strong>Developer:</strong> Engr. Tufail Mabood</li>
    <li><strong>Contact:</strong> <a href="https://wa.me/+923440907874">WhatsApp</a></li>
    <li><strong>Note:</strong> This is an open-source project. Contributions and improvements are welcome.</li>
  </ul>

  <h2>Note</h2>
  <p>
    This utility simplifies preparation of UMAT input properties based on Mazar's damage mechanics model and is ideal for academic and research use with ABAQUS simulations.
  </p>
</body>
</html>
