### Contributing to Brain_Synth

Thank you for your interest in contributing to Brain_Synth!

#### Getting Started

Before you start contributing, please ensure you have read and understood the README(work in progress still) file for an overview of the project.

#### How to Contribute

- Fork the repository to your GitHub account.
- Clone the forked repository to your local machine
- Create a new branch for your feature or bug fix
- Make your changes and commit them
- Push the changes to your forked repository
- Open a pull request (PR) against the main branch of the original repository.

Your PR will be reviewed, and changes may be requested before merging.

#### Code Style Guidelines

Code formatting is handled automatically with [black](https://pypi.org/project/black/) and enforced as part of the build process when opening a PR. Black will automatically be installed as a dependency when running:

```bash
pip install -r requirements.txt
```

You can auto format a specific file by running:

```bash
black <filename>
```

or auto format the entire project by running:

```bash
black .
```

Alternatively, your IDE may have a plugin available to automatically format your code on save.

#### Testing

Include tests for new features or bug fixes.
Ensure all existing tests pass with your changes.

```bash
python tests/tests.py
```

#### Reporting Issues

If you encounter any issues or have feature requests, please open an issue on GitHub. Provide detailed information about the problem and steps to reproduce it.

#### License

This project is licensed under the [GNU General Public License, Version 3.0](LICENSE).
