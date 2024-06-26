# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Nuevamedicion(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, sensor: str=None, fechamuestreo: str=None, unidad: str=None, medicion: float=None):  # noqa: E501
        """Nuevamedicion - a model defined in Swagger

        :param sensor: The sensor of this Nuevamedicion.  # noqa: E501
        :type sensor: str
        :param fechamuestreo: The fechamuestreo of this Nuevamedicion.  # noqa: E501
        :type fechamuestreo: str
        :param unidad: The unidad of this Nuevamedicion.  # noqa: E501
        :type unidad: str
        :param medicion: The medicion of this Nuevamedicion.  # noqa: E501
        :type medicion: float
        """
        self.swagger_types = {
            'sensor': str,
            'fechamuestreo': str,
            'unidad': str,
            'medicion': float
        }

        self.attribute_map = {
            'sensor': 'sensor',
            'fechamuestreo': 'fechamuestreo',
            'unidad': 'unidad',
            'medicion': 'medicion'
        }

        self._sensor = sensor
        self._fechamuestreo = fechamuestreo
        self._unidad = unidad
        self._medicion = medicion

    @classmethod
    def from_dict(cls, dikt) -> 'Nuevamedicion':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The nuevamedicion of this Nuevamedicion.  # noqa: E501
        :rtype: Nuevamedicion
        """
        return util.deserialize_model(dikt, cls)

    @property
    def sensor(self) -> str:
        """Gets the sensor of this Nuevamedicion.

        ID del sensor  # noqa: E501

        :return: The sensor of this Nuevamedicion.
        :rtype: str
        """
        return self._sensor

    @sensor.setter
    def sensor(self, sensor: str):
        """Sets the sensor of this Nuevamedicion.

        ID del sensor  # noqa: E501

        :param sensor: The sensor of this Nuevamedicion.
        :type sensor: str
        """

        self._sensor = sensor

    @property
    def fechamuestreo(self) -> str:
        """Gets the fechamuestreo of this Nuevamedicion.

        Fecha de la medición  # noqa: E501

        :return: The fechamuestreo of this Nuevamedicion.
        :rtype: str
        """
        return self._fechamuestreo

    @fechamuestreo.setter
    def fechamuestreo(self, fechamuestreo: str):
        """Sets the fechamuestreo of this Nuevamedicion.

        Fecha de la medición  # noqa: E501

        :param fechamuestreo: The fechamuestreo of this Nuevamedicion.
        :type fechamuestreo: str
        """

        self._fechamuestreo = fechamuestreo

    @property
    def unidad(self) -> str:
        """Gets the unidad of this Nuevamedicion.

        Unidad de medida  # noqa: E501

        :return: The unidad of this Nuevamedicion.
        :rtype: str
        """
        return self._unidad

    @unidad.setter
    def unidad(self, unidad: str):
        """Sets the unidad of this Nuevamedicion.

        Unidad de medida  # noqa: E501

        :param unidad: The unidad of this Nuevamedicion.
        :type unidad: str
        """

        self._unidad = unidad

    @property
    def medicion(self) -> float:
        """Gets the medicion of this Nuevamedicion.

        Valor de la medición  # noqa: E501

        :return: The medicion of this Nuevamedicion.
        :rtype: float
        """
        return self._medicion

    @medicion.setter
    def medicion(self, medicion: float):
        """Sets the medicion of this Nuevamedicion.

        Valor de la medición  # noqa: E501

        :param medicion: The medicion of this Nuevamedicion.
        :type medicion: float
        """

        self._medicion = medicion
