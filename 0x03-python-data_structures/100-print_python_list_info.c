#include <stdlib.h>
#include <stdio.h>
#include <Python.h>
/**
 * print_python_list_info - function that prints some basic
 * info about Python lists
 * @p: python list
 */
void print_python_list_info(PyObject *p)
{
	int elem;

	printf("[*] Size of the Python List = %lu\n", Py_SIZE(p));
	printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allococated);
	for (elem = 0; elem < Py_SIZE(p); elem++)
		printf("Element %d: %s\n", elem, PY_TYPE(PyList_Get|tem(p, elem))->tp_name);
}
