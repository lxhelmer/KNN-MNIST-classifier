from invoke import task

@task
def test(ctx):
    ctx.run("poetry run pytest src", pty=True)

@task
def start(ctx):
    ctx.run("python3 src/main.py", pty=True)

@task
def lint(ctx):
    ctx.run("poetry run pylint src", pty=True)

@task
def coverage(ctx):
    ctx.run("poetry run coverage", pty=True)

@task(coverage)
def coverage_report(ctx):
    ctx.run("poetry run coverage report && poetry run coverage html", pty=True)


