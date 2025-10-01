        

let
  pkgs = import <nixpkgs> {
			config = {
				allowUnfree = true;
				#cudaSupport = true;
				};
			};
  sympy2jax= pkgs.callPackage ./sympy2jax.nix {pkgs=pkgs;};
in pkgs.mkShell {
  buildInputs = [
    pkgs.libsbml
    pkgs.graphviz
    pkgs.python312
    pkgs.virtualenv
    pkgs.zlib pkgs.expat
    pkgs.stdenv.cc.cc.lib
   




  ];
  shellHook = ''
    # Tells pip to put packages into $PIP_PREFIX instead of the usual locations.
    # See https://pip.pypa.io/en/stable/user_guide/#environment-variables.
    export EXTRA_CCFLAGS="-I/usr/include"
    export PIP_PREFIX=$(pwd)/_build/pip_packages
    export PYTHONPATH="$PIP_PREFIX/${pkgs.python312.sitePackages}:$PYTHONPATH"
    export PATH="$PIP_PREFIX/bin:$PATH"
    export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:${pkgs.zlib}/lib:${pkgs.expat}/lib:${pkgs.stdenv.cc.cc.lib}/lib
    unset SOURCE_DATE_EPOCH

  '';
}

