# GSoC 2026 Explorer

A better way to explore [Google Summer of Code 2026](https://summerofcode.withgoogle.com/programs/2026/organizations). All **185** organizations and their project ideas in one place — with full-text search, advanced filters, and a unified reading experience.

> **184** out of 185 ideas pages successfully scraped — **260** technologies — **509** topics

## Why this exists

The official GSoC website lists organizations but links out to external pages for project ideas — scattered across Google Docs, GitHub wikis, GitLab issues, and various websites. This makes it hard to search, compare, and explore what's available.

**GSoC 2026 Explorer** solves this:

- **Full-text search** — search across all organization names, descriptions, technologies, topics, and project ideas content at once (Cmd+K / Ctrl+K)
- **Advanced combined filters** — filter by technology and topic tags simultaneously, with shareable URLs
- **All ideas in one place** — every ideas page scraped and rendered in a consistent format, with table of contents
- **LLM-ready data** — all data available in JSON and Markdown, ready to feed to language models for analyzing opportunities, matching skills, or generating summaries
- **Fast and responsive** — static site with instant filtering, dark mode, and no page reloads

## Website

**[gsoc-explorer.vercel.app](https://gsoc-explorer.vercel.app)**

To run locally:

```bash
cd web && npm install && npm run build && npx serve out
```

## Repository structure

| Path | Description |
|---|---|
| [`organizations/`](organizations/) | Overview of each organization (tech, topics, links) |
| [`ideas/`](ideas/) | Scraped project ideas in Markdown |
| [`data/`](data/) | JSON data for programmatic access and LLM consumption |
| [`scraper/`](scraper/) | Python scraper source code |
| [`web/`](web/) | Next.js website source code |

## Organizations

| # | Organization | Tech | Ideas |
|---|---|---|---|
| 1 | [52°North Spatial Information Research GmbH](organizations/52north_spatial_information_research_gmbh.md) | javascript, android, java, web services | [View Ideas](ideas/52north_spatial_information_research_gmbh.md) |
| 2 | [AboutCode](organizations/aboutcode.md) | python, javascript, Django+PostgreSQL, C/Rust/Go | [View Ideas](ideas/aboutcode.md) |
| 3 | [Accord Project](organizations/accord_project.md) | python, javascript, json, react | [View Ideas](ideas/accord_project.md) |
| 4 | [AFLplusplus](organizations/aflplusplus.md) | llvm, rust, fuzzing, qemu | [View Ideas](ideas/aflplusplus.md) |
| 5 | [Alaska](organizations/alaska.md) | python, mysql, java, matlab | [View Ideas](ideas/alaska.md) |
| 6 | [AnkiDroid](organizations/ankidroid.md) | android, rust, kotlin, mobile | [View Ideas](ideas/ankidroid.md) |
| 7 | [AOSSIE](organizations/aossie.md) | python, javascript, flutter, Blockchain | [View Ideas](ideas/aossie.md) |
| 8 | [Apache Software Foundation](organizations/apache_software_foundation.md) | c, java, c++ | [View Ideas](ideas/apache_software_foundation.md) |
| 9 | [API Dash](organizations/api_dash.md) | python, react, flutter, typescript | [View Ideas](ideas/api_dash.md) |
| 10 | [ArduPilot](organizations/ardupilot.md) | python, lua, c++, pixhawk | [View Ideas](ideas/ardupilot.md) |
| 11 | [Blender Foundation](organizations/blender_foundation.md) | c, python, opengl, c++ | [View Ideas](ideas/blender_foundation.md) |
| 12 | [Boa](organizations/boa.md) | javascript, rust | [View Ideas](ideas/boa.md) |
| 13 | [BRL-CAD](organizations/brl-cad.md) | python, c/c++, opengl, opencl | [View Ideas](ideas/brl-cad.md) |
| 14 | [C2SI](organizations/c2si.md) | python, java, go, nodejs | [View Ideas](ideas/c2si.md) |
| 15 | [cBioPortal for Cancer Genomics](organizations/cbioportal_for_cancer_genomics.md) | mysql, javascript, java, react | [View Ideas](ideas/cbioportal_for_cancer_genomics.md) |
| 16 | [CCExtractor Development](organizations/ccextractor_development.md) | c, linux, rust, flutter | [View Ideas](ideas/ccextractor_development.md) |
| 17 | [Ceph](organizations/ceph.md) | python, javascript, c++ | [View Ideas](ideas/ceph.md) |
| 18 | [CERN-HSF](organizations/cern-hsf.md) | python, c/c++, data analysis, artificial intelligence | [View Ideas](ideas/cern-hsf.md) |
| 19 | [CGAL Project](organizations/cgal_project.md) | c++, qt | [View Ideas](ideas/cgal_project.md) |
| 20 | [checkstyle](organizations/checkstyle.md) | java, antlr, artificial-intelligence | [View Ideas](ideas/checkstyle.md) |
| 21 | [CircuitVerse.org](organizations/circuitverseorg.md) | javascript, ruby, rails, canvas | [View Ideas](ideas/circuitverseorg.md) |
| 22 | [CNCF](organizations/cncf.md) | prometheus, kubernetes, OpenTelemetry, envoy | [View Ideas](ideas/cncf.md) |
| 23 | [CRIU](organizations/criu.md) | c, python, linux, go | [View Ideas](ideas/criu.md) |
| 24 | [Cuneiform Digital Library Initiative (CDLI)](organizations/cuneiform_digital_library_initiative_cdli.md) | mysql, javascript, docker, php | [View Ideas](ideas/cuneiform_digital_library_initiative_cdli.md) |
| 25 | [D Language Foundation](organizations/d_language_foundation.md) | linux, make, d, windows | [View Ideas](ideas/d_language_foundation.md) |
| 26 | [Dart](organizations/dart.md) | flutter, dart | [View Ideas](ideas/dart.md) |
| 27 | [Data for the Common Good](organizations/data_for_the_common_good.md) | python, javascript, kubernetes, reactjs | [View Ideas](ideas/data_for_the_common_good.md) |
| 28 | [DBpedia](organizations/dbpedia.md) | python, javascript, java, scala | [View Ideas](ideas/dbpedia.md) |
| 29 | [Debian](organizations/debian.md) | python, java, perl, c++ | [View Ideas](ideas/debian.md) |
| 30 | [DeepChem](organizations/deepchem.md) | python, numpy, pytorch, HuggingFace | [View Ideas](ideas/deepchem.md) |
| 31 | [Django Software Foundation](organizations/django_software_foundation.md) | python, django | [View Ideas](ideas/django_software_foundation.md) |
| 32 | [dora-rs](organizations/dora-rs.md) | python, ros, c++, rust | [View Ideas](ideas/dora-rs.md) |
| 33 | [Drupal Association](organizations/drupal_association.md) | mysql, javascript, html, php | [External Link](https://www.drupal.org/project/issues/gsoc?text=2026&status=All&priorities=All&categories=All&version=All&component=All) |
| 34 | [Eclipse Foundation](organizations/eclipse_foundation.md) | java, rtos, eclipsejavaide, jakartaee | [View Ideas](ideas/eclipse_foundation.md) |
| 35 | [EROFS filesystem](organizations/erofs_filesystem.md) | c, android, linux kernel, Containerd | [View Ideas](ideas/erofs_filesystem.md) |
| 36 | [FFmpeg](organizations/ffmpeg.md) | c, git, asm | [View Ideas](ideas/ffmpeg.md) |
| 37 | [FLARE](organizations/flare.md) | python, Sandbox, ida-pro | [View Ideas](ideas/flare.md) |
| 38 | [Fortran-lang](organizations/fortran-lang.md) | python, c++, fortran | [View Ideas](ideas/fortran-lang.md) |
| 39 | [FOSSASIA](organizations/fossasia.md) | c, python, javascript, django | [View Ideas](ideas/fossasia.md) |
| 40 | [FOSSology](organizations/fossology.md) | python, postgresql, c/c++, go | [View Ideas](ideas/fossology.md) |
| 41 | [Free and Open Source Silicon Foundation](organizations/free_and_open_source_silicon_foundation.md) | verilog, vhdl, risc-v, compiler | [View Ideas](ideas/free_and_open_source_silicon_foundation.md) |
| 42 | [FreeCAD](organizations/freecad.md) | python, c++, qt, OpenCASCADE | [View Ideas](ideas/freecad.md) |
| 43 | [Gambit: The package for computation in game theory](organizations/gambit_the_package_for_computation_in_game_theory.md) | python, c++, wxwidgets, visualization | [View Ideas](ideas/gambit_the_package_for_computation_in_game_theory.md) |
| 44 | [Gemini CLI](organizations/gemini_cli.md) | typescript, GenAI, MCP, Software Agent | [View Ideas](ideas/gemini_cli.md) |
| 45 | [Genome Assembly and Annotation](organizations/genome_assembly_and_annotation.md) | python, mysql, docker, pytorch | [View Ideas](ideas/genome_assembly_and_annotation.md) |
| 46 | [GeomScale](organizations/geomscale.md) | python, c++, r, jupyter | [View Ideas](ideas/geomscale.md) |
| 47 | [German Center for Open Source AI](organizations/german_center_for_open_source_ai.md) | python, pytorch, scikit-learn | [View Ideas](ideas/german_center_for_open_source_ai.md) |
| 48 | [Git](organizations/git.md) | shell script, git, c language | [View Ideas](ideas/git.md) |
| 49 | [Global Alliance for Genomics and Health](organizations/global_alliance_for_genomics_and_health.md) | python, postgresql, java, react | [View Ideas](ideas/global_alliance_for_genomics_and_health.md) |
| 50 | [GNOME Foundation](organizations/gnome_foundation.md) | c, linux, rust, gtk | [View Ideas](ideas/gnome_foundation.md) |
| 51 | [GNU Compiler Collection (GCC)](organizations/gnu_compiler_collection_gcc.md) | c/c++, gnu make, gnu autotools | [View Ideas](ideas/gnu_compiler_collection_gcc.md) |
| 52 | [GNU Image Manipulation Program](organizations/gnu_image_manipulation_program.md) | c, GEGL | [View Ideas](ideas/gnu_image_manipulation_program.md) |
| 53 | [GNU Mailman](organizations/gnu_mailman.md) | python, django, rest, sqlalchemy | [View Ideas](ideas/gnu_mailman.md) |
| 54 | [GNU Octave](organizations/gnu_octave.md) | c++, hg | [View Ideas](ideas/gnu_octave.md) |
| 55 | [GNU Project](organizations/gnu_project.md) | c, c++, gcc, autotools | [View Ideas](ideas/gnu_project.md) |
| 56 | [GNU Radio](organizations/gnu_radio.md) | python, c++, qt, simd | [View Ideas](ideas/gnu_radio.md) |
| 57 | [gprMax](organizations/gprmax.md) | python, cuda, openmp, mpi | [View Ideas](ideas/gprmax.md) |
| 58 | [GRAME](organizations/grame.md) | c, javascript, c++, rust | [View Ideas](ideas/grame.md) |
| 59 | [Graphite](organizations/graphite.md) | rust, vulkan, webgpu | [View Ideas](ideas/graphite.md) |
| 60 | [Haiku](organizations/haiku.md) | c++, posix, unix | [View Ideas](ideas/haiku.md) |
| 61 | [Haskell.org](organizations/haskellorg.md) | haskell, ghc | [View Ideas](ideas/haskellorg.md) |
| 62 | [HumanAI](organizations/humanai.md) | python, machine learning, c++, data analysis | [View Ideas](ideas/humanai.md) |
| 63 | [INCF](organizations/incf.md) | python, javascript, java, c++ | [View Ideas](ideas/incf.md) |
| 64 | [International Catrobat Association](organizations/international_catrobat_association.md) | python, javascript, swift, kotlin | [View Ideas](ideas/international_catrobat_association.md) |
| 65 | [Internet Archive](organizations/internet_archive.md) | python, javascript, go, elasticsearch | [View Ideas](ideas/internet_archive.md) |
| 66 | [Invesalius](organizations/invesalius.md) | python, cython, numpy, dicom | [View Ideas](ideas/invesalius.md) |
| 67 | [IOOS](organizations/ioos.md) | python, java, r, Zarr | [View Ideas](ideas/ioos.md) |
| 68 | [JabRef e.V.](organizations/jabref_ev.md) | java, javafx, ai, bibtex | [View Ideas](ideas/jabref_ev.md) |
| 69 | [JBoss Community](organizations/jboss_community.md) | java, react, golang, cloud | [View Ideas](ideas/jboss_community.md) |
| 70 | [JdeRobot](organizations/jderobot.md) | python, ros, gazebo, opencv | [View Ideas](ideas/jderobot.md) |
| 71 | [Jenkins](organizations/jenkins.md) | javascript, java, go, docker | [View Ideas](ideas/jenkins.md) |
| 72 | [Jitsi](organizations/jitsi.md) | javascript, java, react, kotlin | [View Ideas](ideas/jitsi.md) |
| 73 | [Joomla!](organizations/joomla.md) | mysql, javascript, html, php | [View Ideas](ideas/joomla.md) |
| 74 | [Joplin](organizations/joplin.md) | javascript, react, typescript, electron | [View Ideas](ideas/joplin.md) |
| 75 | [JSON Schema](organizations/json_schema.md) | python, javascript, typescript, .net | [View Ideas](ideas/json_schema.md) |
| 76 | [KDE Community](organizations/kde_community.md) | c++, qt, qml, data structures | [View Ideas](ideas/kde_community.md) |
| 77 | [Kiwix](organizations/kiwix.md) | python, c++, nodejs, kotlin | [View Ideas](ideas/kiwix.md) |
| 78 | [KolibriOS Project Team](organizations/kolibrios_project_team.md) | c, assembly, asm, fasm | [View Ideas](ideas/kolibrios_project_team.md) |
| 79 | [Konflux](organizations/konflux.md) | python, go, docker, kubernetes | [View Ideas](ideas/konflux.md) |
| 80 | [Kornia](organizations/kornia.md) | cuda, rust, deep learning, data science | [View Ideas](ideas/kornia.md) |
| 81 | [Kotlin Foundation](organizations/kotlin_foundation.md) | gradle, kotlin, jvm, Parsers & Compilers | [View Ideas](ideas/kotlin_foundation.md) |
| 82 | [Kubeflow](organizations/kubeflow.md) | python, go, kubernetes, typescript | [View Ideas](ideas/kubeflow.md) |
| 83 | [KubeVirt](organizations/kubevirt.md) | golang, grpc | [View Ideas](ideas/kubevirt.md) |
| 84 | [LabLua](organizations/lablua.md) | lua, luarocks, kernel, lunatik | [View Ideas](ideas/lablua.md) |
| 85 | [Learning Equality](organizations/learning_equality.md) | python, javascript, django, vue.js | [View Ideas](ideas/learning_equality.md) |
| 86 | [Learning Unlimited](organizations/learning_unlimited.md) | python, javascript, django, html | [View Ideas](ideas/learning_unlimited.md) |
| 87 | [LibreCube Initiative](organizations/librecube_initiative.md) | python, docker, raspberry pi, micropython | [View Ideas](ideas/librecube_initiative.md) |
| 88 | [LibreHealth](organizations/librehealth.md) | python, javascript, android, java | [View Ideas](ideas/librehealth.md) |
| 89 | [LibreOffice](organizations/libreoffice.md) | python, java, c++ | [View Ideas](ideas/libreoffice.md) |
| 90 | [libssh](organizations/libssh.md) | c, git, ci, ssh | [View Ideas](ideas/libssh.md) |
| 91 | [Liquid Galaxy project](organizations/liquid_galaxy_project.md) | linux, android, nodejs, flutter | [View Ideas](ideas/liquid_galaxy_project.md) |
| 92 | [LLVM Compiler Infrastructure](organizations/llvm_compiler_infrastructure.md) | llvm, c++, clang, mlir | [View Ideas](ideas/llvm_compiler_infrastructure.md) |
| 93 | [Machine Learning for Science (ML4SCI)](organizations/machine_learning_for_science_ml4sci.md) | python, machine learning, c++, data analysis | [View Ideas](ideas/machine_learning_for_science_ml4sci.md) |
| 94 | [MalariaGEN](organizations/malariagen.md) | python, GCS | [View Ideas](ideas/malariagen.md) |
| 95 | [MariaDB](organizations/mariadb.md) | python, javascript, c/c++, perl | [View Ideas](ideas/mariadb.md) |
| 96 | [MDAnalysis](organizations/mdanalysis.md) | python, cython, c/c++ | [View Ideas](ideas/mdanalysis.md) |
| 97 | [Measurement Lab](organizations/measurement_lab.md) | python, javascript, html, sql | [View Ideas](ideas/measurement_lab.md) |
| 98 | [Meshery](organizations/meshery.md) | javascript, golang, kubernetes, ai | [View Ideas](ideas/meshery.md) |
| 99 | [MetaBrainz Foundation Inc](organizations/metabrainz_foundation_inc.md) | python, machine learning, perl, postgres | [View Ideas](ideas/metabrainz_foundation_inc.md) |
| 100 | [MetaCall](organizations/metacall.md) | python, c++, rust, nodejs | [View Ideas](ideas/metacall.md) |
| 101 | [Metaflow](organizations/metaflow.md) | python, javascript, kubernetes | [View Ideas](ideas/metaflow.md) |
| 102 | [Metasploit](organizations/metasploit.md) | c, python, postgresql, ruby | [View Ideas](ideas/metasploit.md) |
| 103 | [MIT App Inventor](organizations/mit_app_inventor.md) | javascript, java, gwt, swift | [View Ideas](ideas/mit_app_inventor.md) |
| 104 | [Mixxx](organizations/mixxx.md) | javascript, c++, qt, pytorch | [View Ideas](ideas/mixxx.md) |
| 105 | [MLLAM](organizations/mllam.md) | python, numpy, pytorch, xarray | [View Ideas](ideas/mllam.md) |
| 106 | [MoFA Org](organizations/mofa_org.md) | python, rust | [View Ideas](ideas/mofa_org.md) |
| 107 | [MoganLab](organizations/moganlab.md) | c++, qt, scheme | [View Ideas](ideas/moganlab.md) |
| 108 | [National Resource for Network Biology (NRNB)](organizations/national_resource_for_network_biology_nrnb.md) | python, javascript, html, css | [View Ideas](ideas/national_resource_for_network_biology_nrnb.md) |
| 109 | [Neovim](organizations/neovim.md) | c, lua | [View Ideas](ideas/neovim.md) |
| 110 | [Neuroinformatics Unit](organizations/neuroinformatics_unit.md) | python, numpy, pytorch, Scipy | [View Ideas](ideas/neuroinformatics_unit.md) |
| 111 | [Neutralinojs](organizations/neutralinojs.md) | c, javascript, node.js, c++ | [View Ideas](ideas/neutralinojs.md) |
| 112 | [NixOS Foundation](organizations/nixos_foundation.md) | git, nix | [View Ideas](ideas/nixos_foundation.md) |
| 113 | [NumFOCUS](organizations/numfocus.md) | python, c++, r, julia | [View Ideas](ideas/numfocus.md) |
| 114 | [omegaUp](organizations/omegaup.md) | python, mysql, php, typescript | [View Ideas](ideas/omegaup.md) |
| 115 | [Open Food Facts](organizations/open_food_facts.md) | python, javascript, machine learning, perl | [View Ideas](ideas/open_food_facts.md) |
| 116 | [Open Genome Informatics](organizations/open_genome_informatics.md) | python, react, r-project, graph | [View Ideas](ideas/open_genome_informatics.md) |
| 117 | [Open HealthCare Network](organizations/open_healthcare_network.md) | python, django, react, typescript | [View Ideas](ideas/open_healthcare_network.md) |
| 118 | [Open Robotics](organizations/open_robotics.md) | python, ros, gazebo, c++ | [View Ideas](ideas/open_robotics.md) |
| 119 | [Open Science Initiative for Perfusion Imaging](organizations/open_science_initiative_for_perfusion_imaging.md) | python, github | [View Ideas](ideas/open_science_initiative_for_perfusion_imaging.md) |
| 120 | [Open Science Labs](organizations/open_science_labs.md) | python, javascript, llvm, c++ | [View Ideas](ideas/open_science_labs.md) |
| 121 | [Open Technologies Alliance - GFOSS](organizations/open_technologies_alliance_-_gfoss.md) | javascript, c/c++, nodejs, python 3 | [View Ideas](ideas/open_technologies_alliance_-_gfoss.md) |
| 122 | [Open Transit Software Foundation](organizations/open_transit_software_foundation.md) | android, java, golang, docker | [View Ideas](ideas/open_transit_software_foundation.md) |
| 123 | [OpenAFS](organizations/openafs.md) | c, python, javascript, git | [View Ideas](ideas/openafs.md) |
| 124 | [OpenAstronomy](organizations/openastronomy.md) | c, python, c++, julia | [View Ideas](ideas/openastronomy.md) |
| 125 | [OpenELIS Global](organizations/openelis_global.md) | postgresql, javascript, java, react | [View Ideas](ideas/openelis_global.md) |
| 126 | [OpenMRS](organizations/openmrs.md) | mysql, javascript, java, reactjs | [View Ideas](ideas/openmrs.md) |
| 127 | [OpenMS Inc](organizations/openms_inc.md) | python, cython, c++, pytorch | [View Ideas](ideas/openms_inc.md) |
| 128 | [OpenStreetMap](organizations/openstreetmap.md) | python, javascript, c++, docker | [View Ideas](ideas/openstreetmap.md) |
| 129 | [openSUSE Project](organizations/opensuse_project.md) | python, c/c++, go, ruby | [View Ideas](ideas/opensuse_project.md) |
| 130 | [OpenVINO Toolkit](organizations/openvino_toolkit.md) | python, c++, arm, x86 | [View Ideas](ideas/openvino_toolkit.md) |
| 131 | [OpenWISP](organizations/openwisp.md) | python, javascript, django, lua | [View Ideas](ideas/openwisp.md) |
| 132 | [Oppia Foundation](organizations/oppia_foundation.md) | python, google app engine, angular, typescript | [View Ideas](ideas/oppia_foundation.md) |
| 133 | [OSGeo (Open Source Geospatial Foundation)](organizations/osgeo_open_source_geospatial_foundation.md) | c, python, javascript, java | [View Ideas](ideas/osgeo_open_source_geospatial_foundation.md) |
| 134 | [OWASP Foundation](organizations/owasp_foundation.md) | python, javascript, java, ZAP | [View Ideas](ideas/owasp_foundation.md) |
| 135 | [PEcAn Project](organizations/pecan_project.md) | r, docker, api, geospatial | [View Ideas](ideas/pecan_project.md) |
| 136 | [Pharo Consortium](organizations/pharo_consortium.md) | git, smalltalk, pharo, spec | [View Ideas](ideas/pharo_consortium.md) |
| 137 | [PostgreSQL](organizations/postgresql.md) | c, python, postgresql, javascript | [View Ideas](ideas/postgresql.md) |
| 138 | [preCICE](organizations/precice.md) | c, python, shell, c++ | [View Ideas](ideas/precice.md) |
| 139 | [Processing Foundation](organizations/processing_foundation.md) | javascript, java, typescript, webgl | [View Ideas](ideas/processing_foundation.md) |
| 140 | [Project Mesa](organizations/project_mesa.md) | python, gis, object oriented programming, LLMs | [View Ideas](ideas/project_mesa.md) |
| 141 | [Python Software Foundation](organizations/python_software_foundation.md) | python, javascript | [View Ideas](ideas/python_software_foundation.md) |
| 142 | [QC-Devs](organizations/qc-devs.md) | python, github, c++, julia | [View Ideas](ideas/qc-devs.md) |
| 143 | [QEMU](organizations/qemu.md) | c, python, linux, rust | [View Ideas](ideas/qemu.md) |
| 144 | [Qubes OS](organizations/qubes_os.md) | c, python, xen | [View Ideas](ideas/qubes_os.md) |
| 145 | [R project for statistical computing](organizations/r_project_for_statistical_computing.md) | c, javascript, c++, r-project | [View Ideas](ideas/r_project_for_statistical_computing.md) |
| 146 | [Rizin](organizations/rizin.md) | c, python, go, c++ | [View Ideas](ideas/rizin.md) |
| 147 | [rocket.chat](organizations/rocketchat.md) | javascript, typescript, node, LLM | [View Ideas](ideas/rocketchat.md) |
| 148 | [RTEMS Project](organizations/rtems_project.md) | python, c/c++, assembly, posix | [View Ideas](ideas/rtems_project.md) |
| 149 | [Ruby](organizations/ruby.md) | c, java, ruby on rails, ruby | [View Ideas](ideas/ruby.md) |
| 150 | [SageMath](organizations/sagemath.md) | python, cython | [View Ideas](ideas/sagemath.md) |
| 151 | [ScummVM](organizations/scummvm.md) | python, opengl, c++, assembly | [View Ideas](ideas/scummvm.md) |
| 152 | [St. Jude Children's Research Hospital](organizations/st_jude_childrens_research_hospital.md) | python, rust, simd, WDL | [View Ideas](ideas/st_jude_childrens_research_hospital.md) |
| 153 | [stdlib](organizations/stdlib.md) | c, javascript, node.js, typescript | [View Ideas](ideas/stdlib.md) |
| 154 | [Ste\|\|ar group](organizations/stear_group.md) | c++, hpc | [View Ideas](ideas/stear_group.md) |
| 155 | [Stichting SU2](organizations/stichting_su2.md) | python, c++ | [View Ideas](ideas/stichting_su2.md) |
| 156 | [Submitty](organizations/submitty.md) | python, postgresql, javascript, c++ | [View Ideas](ideas/submitty.md) |
| 157 | [Sugar Labs](organizations/sugar_labs.md) | python, gtk, typescript, javascipt | [View Ideas](ideas/sugar_labs.md) |
| 158 | [SW360](organizations/sw360.md) | java, react, couchdb, SpringBoot | [View Ideas](ideas/sw360.md) |
| 159 | [Swift](organizations/swift.md) | c++, cmake, swift | [View Ideas](ideas/swift.md) |
| 160 | [SymPy](organizations/sympy.md) | python, numpy, jupyter | [View Ideas](ideas/sympy.md) |
| 161 | [Synfig](organizations/synfig.md) | python, c++, gtk, gtkmm | [View Ideas](ideas/synfig.md) |
| 162 | [TARDIS RT Collaboration](organizations/tardis_rt_collaboration.md) | python, numba, numpy, jupyter | [View Ideas](ideas/tardis_rt_collaboration.md) |
| 163 | [The FreeBSD Project](organizations/the_freebsd_project.md) | c, llvm, assembly, make | [View Ideas](ideas/the_freebsd_project.md) |
| 164 | [The Honeynet Project](organizations/the_honeynet_project.md) | python, javascript, django, go | [View Ideas](ideas/the_honeynet_project.md) |
| 165 | [The JPF team](organizations/the_jpf_team.md) | android, java, distributed systems, jvm | [View Ideas](ideas/the_jpf_team.md) |
| 166 | [The Julia Language](organizations/the_julia_language.md) | machine learning, julia, data science, compilers | [View Ideas](ideas/the_julia_language.md) |
| 167 | [The Libreswan Project](organizations/the_libreswan_project.md) | c, kernel, nss, RFCs | [View Ideas](ideas/the_libreswan_project.md) |
| 168 | [The Linux Foundation](organizations/the_linux_foundation.md) | c, linux, cups, ai | [View Ideas](ideas/the_linux_foundation.md) |
| 169 | [The Mifos Initiative](organizations/the_mifos_initiative.md) | android, java, kotlin, spring | [View Ideas](ideas/the_mifos_initiative.md) |
| 170 | [The NetBSD Foundation](organizations/the_netbsd_foundation.md) | c, shell script, make, unix | [View Ideas](ideas/the_netbsd_foundation.md) |
| 171 | [The ns-3 Network Simulator Project](organizations/the_ns-3_network_simulator_project.md) | python, django, c++ | [View Ideas](ideas/the_ns-3_network_simulator_project.md) |
| 172 | [The OpenROAD Initiative](organizations/the_openroad_initiative.md) | python, verilog, c++, tcl | [View Ideas](ideas/the_openroad_initiative.md) |
| 173 | [The P4 Language Consortium](organizations/the_p4_language_consortium.md) | llvm, c++, linux kernel, mlir | [View Ideas](ideas/the_p4_language_consortium.md) |
| 174 | [The Rust Foundation](organizations/the_rust_foundation.md) | python, rust | [View Ideas](ideas/the_rust_foundation.md) |
| 175 | [Tiled](organizations/tiled.md) | c++, qt | [View Ideas](ideas/tiled.md) |
| 176 | [Typelevel](organizations/typelevel.md) | linux, node.js, jvm, scala | [View Ideas](ideas/typelevel.md) |
| 177 | [UC OSPO](organizations/uc_ospo.md) | python, javascript, c/c++, machine learning | [View Ideas](ideas/uc_ospo.md) |
| 178 | [Unikraft](organizations/unikraft.md) | c, xen, golang, kvm | [View Ideas](ideas/unikraft.md) |
| 179 | [United Nations Office of Information Communication Technology](organizations/united_nations_office_of_information_communication_technology.md) | python, javascript, css | [View Ideas](ideas/united_nations_office_of_information_communication_technology.md) |
| 180 | [Uramaki LAB](organizations/uramaki_lab.md) | python, javascript, html, css | [View Ideas](ideas/uramaki_lab.md) |
| 181 | [VideoLAN](organizations/videolan.md) | c, c++, qt, assembly | [View Ideas](ideas/videolan.md) |
| 182 | [Wagtail](organizations/wagtail.md) | python, javascript, django | [View Ideas](ideas/wagtail.md) |
| 183 | [webpack](organizations/webpack.md) | javascript, typescript, node | [View Ideas](ideas/webpack.md) |
| 184 | [Wikimedia Foundation](organizations/wikimedia_foundation.md) | javascript, html, php, css | [View Ideas](ideas/wikimedia_foundation.md) |
| 185 | [Zulip](organizations/zulip.md) | python, django, flutter, css | [View Ideas](ideas/zulip.md) |

## How the data was collected

A Python scraper queries the [GSoC public API](https://summerofcode.withgoogle.com/api/program/2026/organizations/), then fetches each organization's ideas page and converts it to Markdown:

- **GitHub** blob/wiki/gist URLs are converted to raw URLs for clean Markdown
- **Google Docs** are exported as HTML and converted
- **GitHub/GitLab issues** are fetched via CLI/API
- **HTML pages** are extracted via [trafilatura](https://github.com/adbar/trafilatura) or [markdownify](https://github.com/matthewwithanm/python-markdownify)
- **JS-rendered pages** are handled by [Playwright](https://playwright.dev/) headless browser

See [`scraper/`](scraper/) for the source code.

## License

The scraped content belongs to the respective organizations. The scraper and website code in this repository are provided as-is for educational purposes.
