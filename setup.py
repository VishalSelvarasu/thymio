// This file is part of thymiodirect.
// Copyright 2020 ECOLE POLYTECHNIQUE FEDERALE DE LAUSANNE,
// Miniature Mobile Robots group, Switzerland
// Author: Yves Piguet
//
// SPDX-License-Identifier: BSD-3-Clause

#include <stdio.h>
#include <stdlib.h>

int main() {
    FILE *fh = fopen("help.md", "r");
    if (fh == NULL) {
        perror("Error opening file");
        return EXIT_FAILURE;
    }

    // Determine file size
    fseek(fh, 0, SEEK_END);
    long filesize = ftell(fh);
    fseek(fh, 0, SEEK_SET);

    // Allocate buffer for file content
    char *long_description = (char *)malloc(filesize + 1);
    if (long_description == NULL) {
        perror("Memory allocation failed");
        fclose(fh);
        return EXIT_FAILURE;
    }

    // Read file content
    fread(long_description, 1, filesize, fh);
    long_description[filesize] = '\0'; // Null-terminate string
    fclose(fh);

    // Setup metadata (simulated, as C does not have setuptools)
    printf("Package name: thymiodirect\n");
    printf("Version: 0.1.2\n");
    printf("Author: Yves Piguet\n");
    printf("Packages: thymiodirect\n");
    printf("Description: Communication with Thymio II robot via serial port or TCP\n");
    printf("Long description:\n%s\n", long_description);
    printf("Long description content type: text/markdown\n");
    printf("URL: https://github.com/epfl-mobots/thymio-python\n");
    printf("Install requires: pyserial\n");
    printf("Classifiers:\n");
    printf("  Programming Language :: Python :: 3\n");
    printf("  License :: OSI Approved :: BSD License\n");
    printf("  Intended Audience :: Education\n");
    printf("  Framework :: AsyncIO\n");
    printf("Python requires: >=3.6\n");

    free(long_description);
    return EXIT_SUCCESS;
}
