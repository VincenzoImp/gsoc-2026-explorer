# libssh — Project Ideas

**Source:** https://www.libssh.org/development/google-summer-of-code/
**Scraped:** 2026-02-22T23:28:47.565877

---

## Contributors guidance

### The application process consists of next steps:

- Become acquainted with application process for GSoC.
- Join to gsoc mailing list:
[https://groups.google.com/group/google-summer-of-code-announce](https://groups.google.com/group/google-summer-of-code-announce) - Join libssh mailing list:
[https://www.libssh.org/communication/](/ideas/libssh/communication) - Search mentor for chosen project in mailing list discuss or propose your own project and find a mentor for it.
- Submit the application/proposal including all requirements at the Google Summer of Code Site.

### Requirements before starting search for mentor:

- Clone and build libssh sources:
[https://www.libssh.org/development/](/ideas/libssh/development) - Review existing issues in bug tracker and try to solve some simpler one, providing a merge request on gitlab mirror
[https://gitlab.com/libssh/libssh-mirror/-/issues](https://gitlab.com/libssh/libssh-mirror/-/issues). This is REQUIRED and project proposals without any prior interactions and non-trivial MR will not be considered. - Prepare answers to questions about own participation in project.

### Application requirements/recommendations:

- All applications
*must*go through Google’s application system; we can’t accept any application unless it is submitted there. - Use a descriptive title in Google’s system. Good example: “libssh: Improve SSH connection fuzzing” Bad example: “My gsoc project”
- Make it easy for your mentors to give you feedback. If you’re using Google docs, enable comments and submit a “draft” (we can’t see the “final” versions until applications close). If you’re using a format that doesn’t accept comments, make sure your email is on the document and don’t forget to check for feedback!
- Use the following template for the your project application. It will help you to answer the questions we want to hear answers for and prepare yourself for the project itself:
[https://docs.google.com/document/d/1H1BDf0gZZkPwTOKuu7cOsPq40DBuOCY8qcF8e49pXUY](https://docs.google.com/document/d/1H1BDf0gZZkPwTOKuu7cOsPq40DBuOCY8qcF8e49pXUY)

### AI usage

If you are using any AI/LLM tools to help you with the contributions or proposal, you need to provide a description of the tools used and extent of this use (ex. Proofreading proposal using XXX, Code review by YYY, Coding assistant ZZZ to draft test cases …)”. That said, AI usage is not bad, but it needs to be used as and addition to your intelligence and not a replacement.

### GSoC libssh organization administrators:

- Jakub Jelen (jakuje on Matrix)
- Sahana Prasad (saprasad on Matrix)
- Andreas Schneider (asn on Matrix)

### libssh mentors:

- Jakub Jelen (jakuje on Matrix)
- Sahana Prasad (saprasad on Matrix)
- Eshan Kelkar (eshan_k on Matrix)

## Project ideas

### Introduce Rust into libssh

libssh in written in C which has it strength and weaknesses. It is fast and you have a lot of freedom but it is also easy to “shoot yourself in the foot”. To improve memory safety we should start replacing the core parts with Rust.

The project would involve two things. Create a CMake module to deal with Rust and convert string.c to string.rs. If time permits buffer.c to buffer.rs. The plan would be to bring the CMake module upstream.

- Difficult: Medium
- Project length: 350 hours
- Language(s): Good knowledge of C and/or Rust
- Possible Mentors: Jakub Jelen and Andreas Schneider
- References:
[CMake Rust Integration Plan](https://hackmd.io/@asn/r19DwWZwbx)

### OpenSSH-compatible CLI

The libssh is provided as a library and only provided binaries are examples implementing either specific client or server examples without an attempt to implement a CLI that can support most of the OpenSSH’s CLI use cases and could be used as a drop-in replacement. The libssh should already support most of the use cases (and if not, new issues should be opened and implemented). Similar exercise can be done for server, but there will many more gaps.

- Difficulty: Medium
- Project length: 350 hours
- Language(s): Good knowledge of C or Rust
- Possible Mentors: Jakub Jelen
- References:
- Manual page for ssh:
[https://linux.die.net/man/1/ssh](https://linux.die.net/man/1/ssh)

- Manual page for ssh:

### Improve configuration compatibility with OpenSSH

The libssh is trying to be compatible with the OpenSSH configuration files to make the experience for our users as smooth as possible to be able to use only one configuration file for both. But OpenSSH configuration file options grow in complexity and we are not catching up with all the corner cases, which sometimes got reported to us. This project is about understanding the SSH configuration, how it is handled by OpenSSH and adjusting the libssh configuration parser to match as closely as possible, including adding a automated test coverage that can compare results with the OpenSSH parser.

It might be possible to create a fuzzer for the configuration file, that would feed the inputs into both openssh and libssh to verify they result in the same effective configuration.

- Difficulty: Hard
- Project length: 350 hours
- Language(s): Good knowledge of C, understanding of fuzzing testing is a plus
- Possible Mentors: Jakub Jelen
- References:
- Manual page for ssh_config:
[https://linux.die.net/man/5/ssh_config](https://linux.die.net/man/5/ssh_config)

- Manual page for ssh_config:

### Design and implement API to communicate with SSH-Agent

The libssh can communicate with an ssh-agent/pageant, but only internally in the function `ssh_userauth_agent()`

. This has disadvantage that the agent can not be used on the server, the agent can not be used for signing data (sshsig) and there is no API to operate on the agent from the calling application (list keys, add keys, …).

The rough idea is to have a new set of APIs that will allow list the keys, returning opaque ssh_key structures, that will transparently redirect the key operation to agent.

- Difficulty: Medium
- Project length: 175 hours
- Language(s): Good knowledge of C, API design understanding, knowledge about ssh-agent is a plus
- Possible Mentors: Jakub Jelen
- References:

## Completed projects

### Support for FIDO/U2F keys on the client side (2025)

The server side support (signature verification) and key type definitions are in place so authenticating using these keys from openssh client to libssh server should already work. But the libssh clients can not use the U2F based keys as well as it can not be used to enroll the hardware for authentication with ssh.

The project should involve adding code paths to create U2F signatures, as well as possibility to test them without the actual hardware in the CI. Here we can get inspiration from OpenSSH, as they provide sk-dummy.so, which can simulate fido/u2f devices. This is packaged in Fedora.

- Difficulty: Medium
- Project length: 350 hours
- Language(s): Good knowledge of C, knowledge about elliptic curves cryptography or u2f is a plus 😉
- Possible Mentors: Jakub Jelen, Sahana Prasad, Eshan Kelkar
- References:
- Student: Praneeth Sarode
[https://darkphoenix42.github.io/posts/gsoc-2025/](https://darkphoenix42.github.io/posts/gsoc-2025/)

### Support for OpenSSH certificates (2024)

The libssh supports OpenSSH certificates as opaque blobs alongside the client keys only to pass them along with the key to some compatible server to verify the authentication. This is ok for basic interoperability with OpenSSH servers configured to accept certificates signed with Users CA, but it does not cover the server use cases (authenticating users), nor the Hosts CA (authenticating servers to clients) use case at all.

- Difficulty: Medium
- Project length: 350 hours
- Language(s): Good knowledge of C, knowledge about certificates is a plus
- Mentors: Jakub Jelen, Sahana Prasad, Eshan Kelkar
- References:
- Student: Francesco Rollo
[https://medium.com/@eferollo/my-google-summer-of-code-2024-journey-with-libssh-802e72f935e3](https://medium.com/@eferollo/my-google-summer-of-code-2024-journey-with-libssh-802e72f935e3)

### Test coverage for GSSAPI Authentication (2024)

The libssh supports GSSAPI authentication for ages. But there is no automated test coverage for neither client nor server, making the code Schrodinger code (both working but more likely broken). This project involves learning how the GSSAPI authentication in SSH protocol works, proposing test cases and implementing them inside of the upstream testsuite with help of the [cwrap](https://cwrap.org/) wrappers. Stretch goal is looking into the GSSAPI Key exchange defined in the same RFC and [RFC8732](https://datatracker.ietf.org/doc/html/rfc8732) and testing it well.

- Difficulty: Medium
- Project length: 350 hours
- Language(s): Good knowledge of C, knowledge about kerberos and GSSAPI is a plus
- Mentors: Jakub Jelen, Sahana Prasad, Eshan Kelkar
- References:
- Student: Gauravsingh Sisodia
[https://xaerru.github.io/gsoc24/](https://xaerru.github.io/gsoc24/)

### async SFTP client (2023)

The SFTP implementation in libssh requires application to call libssh API to send each chunk of data, which is not the fastest option. Our idea is that libssh should provide an API similar to io_uring, where you set up the transfer of the file and libssh will take care of the rest.

- Difficulty: hard
- Project length: 350 hours
- Language(s): Good knowledge of C, network programming and IO handling
- Mentors: Sahana Prasad, Jakub Jelen, Norbert Pocs
- References:
- Student: Eshan Kelkar
[https://summerofcode.withgoogle.com/programs/2023/projects/CdkiroFH](https://summerofcode.withgoogle.com/programs/2023/projects/CdkiroFH)

### Support for OpenSSH connection multiplexing (2023)

The OpenSSH supports sharing several sessions over a single TCP connection, which makes opening new channels faster from cli. The usage of the same MUX protocol is not mandatory, but as we already work with openssh configuration files so, it would probably make sense to implement it in compatible way.

- Difficulty: medium/hard
- Project length: 175 hours
- Language(s): Good knowledge of C, knowledge about communication between processes is a plus 😉
- Mentors: Norbert Pocs, Sahana Prasad
- References:
- Student: Ahsen Kamal
[https://summerofcode.withgoogle.com/programs/2023/projects/GdK87jbe](https://summerofcode.withgoogle.com/programs/2023/projects/GdK87jbe)

**Callback based sftp server** (2022)

Currently, the sftp server implementation is based on a huge switch handling all the possible messages. Changing to callback-based model can provide much better customization by the library users

- Difficulty: medium
- Project length: 175 hours
- Language(s): Good knowledge of C and network programming
- Mentors: Jakub Jelen
- References:
- The ssh server in libssh is using callback to handle various SSH protocol messages or authentication types

- Student: Zeyu Sheng
[https://summerofcode.withgoogle.com/programs/2022/projects/Hm79LwKE](https://summerofcode.withgoogle.com/programs/2022/projects/Hm79LwKE)
