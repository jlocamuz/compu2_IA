from celery_config import app


@app.task
def add(n, m):
	return n + m


@app.task(serializer='pickle')
def actualizar_neurona(dato, neurona, red, bias, lr):
	if neurona.capa == 0:
		entrada = [bias] + list(dato[:-1])
	else:
		# CAPAS INTERMEDIAS
		resultados_anteriores = [i.resultado for i in red[neurona.capa - 1]]
		entrada = [bias] + resultados_anteriores
	neurona.sumatoria(entrada)
	neurona.error = dato[-1] - neurona.resultado
	neurona.actualizar_pesos(lr, entrada)


