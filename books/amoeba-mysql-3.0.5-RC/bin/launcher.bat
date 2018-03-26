@rem ----------------------------------------------------------------------------
@rem ����Amoeba�Ľű�
@rem
@rem ��Ҫ�������»���������
@rem
@rem    JAVA_HOME           - JDK�İ�װ·��
@rem
@rem ----------------------------------------------------------------------------
@echo off
if "%OS%"=="Windows_NT" setlocal

:CHECK_JAVA_HOME
if not "%JAVA_HOME%"=="" goto SET_AMOEBA_HOME

echo.
echo ����: �������û���������JAVA_HOME����ָ��JDK�İ�װ·��
echo.
goto END

:SET_AMOEBA_HOME
set AMOEBA_HOME=%~dp0..
if not "%AMOEBA_HOME%"=="" goto START_AMOEBA

echo.
echo ����: �������û���������AMOEBA_HOME����ָ��Amoeba�İ�װ·��
echo.
goto END

:START_AMOEBA


@rem  FOR /F "tokens=1,* delims=.=" %%G IN (%AMOEBA_HOME%\jvm.properties) DO (
@rem 	 set %%G=%%H 
@rem 	 echo %%G=$ %%H
@rem )


set DEFAULT_OPTS=-server -Xms256m -Xmx1024m -Xss128k
set DEFAULT_OPTS=%DEFAULT_OPTS% -XX:+HeapDumpOnOutOfMemoryError -XX:+AggressiveOpts -XX:+UseParallelGC -XX:+UseBiasedLocking -XX:NewSize=64m
set DEFAULT_OPTS=%DEFAULT_OPTS% "-Damoeba.home=%AMOEBA_HOME%"
set DEFAULT_OPTS=%DEFAULT_OPTS% "-Dproject.home=%AMOEBA_HOME%"
set DEFAULT_OPTS=%DEFAULT_OPTS% "-Dproject.name=Amoeba-MySQL"
set DEFAULT_OPTS=%DEFAULT_OPTS% "-Dclassworlds.conf=%AMOEBA_HOME%\bin\launcher.classpath"

set JAVA_EXE="%JAVA_HOME%\bin\java.exe"
set CLASSPATH="%AMOEBA_HOME%\lib\plexus-classworlds-2.4.2-HEXNOVA.jar"
set MAIN_CLASS="org.codehaus.classworlds.Launcher"

%JAVA_EXE% %DEFAULT_OPTS% -classpath %CLASSPATH% %MAIN_CLASS% %*

:END
if "%OS%"=="Windows_NT" endlocal
pause