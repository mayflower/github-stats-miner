let
  callPackage = (import <nixpkgs> {}).callPackage;
in
callPackage (
{ python3 }:
python3.pkgs.buildPythonApplication rec {
  name = "github-stats-miner";
  src = ./.;

  propagatedBuildInputs = with python3.pkgs; [
    jupyter pandas git-pandas joblib github3_py
  ];
}
) {}
