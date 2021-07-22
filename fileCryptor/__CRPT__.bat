@ECHO OFF

REM Using Local EnvVariable
SETLOCAL

REM set value to OPTION. p is input by user.
set /p OPTION=

if not %OPTION% == e (
    if not %OPTION% == d (
        EXIT
    )
)

set PYTHON=python

if %OPTION% == e (
    %PYTHON% .\__ENC__
)

if %OPTION% == d (
    %PYTHON% .\__DEC__
)

ENDLOCAL
PAUSE