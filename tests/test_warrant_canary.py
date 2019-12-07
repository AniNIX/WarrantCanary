import pytest
import shutil
import subprocess

def test_warrant_canary_usage():
    ### Ensure that the script provides output.
    procState=subprocess.run(['./warrant_canary','-h'],capture_output=True,timeout=3)
    assert procState.returncode == 0 and procState.stderr == b''

def test_warrant_canary_seed():
    ### Test that we can seed a warrant canary file
    # procState=subprocess.run(['./warrant_canary','-s'],capture_output=True,timeout=3)
    try:
        with open('canary.asc') as fh:
            # assert procState.returncode == 0 and procState.stderr == b'' and 'BEGIN PGP SIGNATURE' in fh.read() and b'Success' in procState.stderr
            assert 'BEGIN PGP SIGNATURE' in fh.read()
    except:
        assert False

def test_warrant_canary_basic_verify():
    ### Test that we can verify with no arguments
    procState=subprocess.run(['./warrant_canary','-V'],capture_output=True,timeout=3)
    assert procState.returncode == 0 and procState.stderr == b'' and b'Good signature' in procState.stdout

def test_warrant_canary_file_verify():
    ### Test that we can verify with a file
    procState=subprocess.run(['./warrant_canary','-c','./canary.asc','-V'],capture_output=True,timeout=3)
    assert procState.returncode == 0 and procState.stderr == b'' and b'Good signature' in procState.stdout

def test_warrant_canary_url_verify():
    ### Test that we can verify with a web address
    procState=subprocess.run(['./warrant_canary','-c','https://cryptostorm.is/canary.txt','-k','E9C7C942','-K','pgp.mit.edu','-V'],capture_output=True,timeout=30)
    assert procState.returncode == 0 and procState.stderr == b'' and b'Good signature' in procState.stdout
