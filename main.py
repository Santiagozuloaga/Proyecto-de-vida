#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S.O.P. V. 2.0 - Sistema Operativo Personal
Backend: Estructura de Datos del Proyecto de Vida
Estudiante: Grado 10° | Edad: 16 años
Asignatura: Ética

INSTRUCCIONES DE USO:
1. Abrir terminal/CMD
2. Navegar a la carpeta: cd ruta/del/proyecto
3. Ejecutar: python main.py
4. Seguir las instrucciones del menú
"""

# ============================================
# ESTRUCTURA DE DATOS PRINCIPAL
# ============================================

PROYECTO_DE_VIDA = {
    # Información Personal
    "metadata": {
        "nombre": "S.O.P. - Sistema Operativo Personal",
        "version": "2.0",
        "estudiante": {
            "grado": "10°",
            "edad": 16,
            "rol": "Ingeniero de mi propio destino"
        },
        "fecha_inicio": "2024",
        "estado": "EN_EJECUCION"
    },
    
    # Filosofía Central
    "kernel": {
        "lema_principal": "Si vis pacem, para bellum",
        "traduccion": "Si quieres la paz, prepárate para la guerra",
        "filosofia": "Estoicismo",
        "principios": [
            "Dicotomía del Control",
            "Disciplina Blindada",
            "Resiliencia del Tanque",
            "Kaizen (Mejora Continua)"
        ],
        "algoritmo_resiliencia": """
def Resiliencia(adversidad):
    if adversidad == "Falla Crítica":
        ejecutar("Plan_de_Recuperacion")
        aplicar("Dicotomia_del_Control")
    
    while obstaculos_presentes:
        mantener("Disciplina_Blindada")
        fortalecer("Caracter")
    
    return "Hombre_Estoico"
        """
    },
    
    # Metas a Corto Plazo (1-3 meses)
    "metas_corto_plazo": {
        "espiritual": {
            "objetivo": "Calibración de la Fe",
            "acciones": [
                "Práctica diaria de la Dicotomía del Control (Estoicismo)",
                "Tiempo de silencio para reconectar emociones",
                "Definición de tu fe (Dios vs. Instituciones)"
            ],
            "prioridad": "ALTA"
        },
        "afectivo_emocional": {
            "objetivo": "Anulación del Código V. 1.0",
            "acciones": [
                "Descontinuar la máscara y la grosería",
                "Iniciar la práctica de la tolerancia y la amabilidad",
                "Establecer transparencia (dejar de mentir por miedo)"
            ],
            "prioridad": "CRÍTICA"
        },
        "intelectual": {
            "objetivo": "Activación del Foco",
            "acciones": [
                "Reenfocar la concentración de videojuegos a temas complejos",
                "Inglés Básico: Estudio diario (mínimo 15 min)",
                "Alemán: Mantener el avance lingüístico"
            ],
            "prioridad": "ALTA"
        },
        "ocupacional": {
            "objetivo": "Liquidación de Deuda Académica",
            "acciones": [
                "PRIORIDAD MÁXIMA a Matemáticas y deudas críticas",
                "Iniciar desarrollo de talentos (música, dibujo, escritura) como disciplina"
            ],
            "prioridad": "CRÍTICA",
            "nota": "Estabilizar el rendimiento académico es FUNDAMENTAL"
        },
        "economico": {
            "objetivo": "Gestión de Riesgo",
            "acciones": [
                "Estabilizar situación familiar generada por el conflicto",
                "No generar nuevos gastos o deudas innecesarias"
            ],
            "prioridad": "ALTA"
        },
        "familiar": {
            "objetivo": "Desescalada de Conflictos",
            "acciones": [
                "Usar disculpa estratégica (por los gritos)",
                "Ejecución inmediata del Plan de Recuperación como prueba de respeto"
            ],
            "prioridad": "CRÍTICA"
        },
        "corporal": {
            "objetivo": "Mantenimiento del Hardware",
            "acciones": [
                "Reinicio del Sistema (Sueño): Priorizar 7-8 horas de descanso",
                "Bloqueo Activo: Implementar bloqueo contra pornografía para proteger foco mental"
            ],
            "prioridad": "ALTA"
        }
    },
    
    # Metas a Medio Plazo (6-12 meses)
    "metas_medio_plazo": {
        "intelectual": {
            "objetivo": "Compilación Avanzada",
            "acciones": [
                "Lograr fluidez en Inglés (Sintaxis V. 2.0)",
                "Alcanzar nivel conversacional en Alemán",
                "Completar certificación técnica en Ingeniería"
            ]
        },
        "afectivo_emocional": {
            "objetivo": "Refuerzo de Empatía",
            "acciones": [
                "Fortalecer 2-3 relaciones clave (familiares/amigos) con honestidad",
                "Mejorar manejo de interacciones sociales"
            ]
        },
        "ocupacional": {
            "objetivo": "Diseño del Camino",
            "acciones": [
                "Confirmar vocación de Ingeniería mediante experiencias prácticas",
                "Establecer contactos profesionales",
                "Desarrollar proyectos personales"
            ]
        }
    },
    
    # Metas a Largo Plazo (1-3 años)
    "metas_largo_plazo": {
        "espiritual": {
            "objetivo": "Hombre Estoico",
            "descripcion": "Vivir la Resiliencia del Tanque y la Disciplina Blindada. Coherencia entre propósito y carácter."
        },
        "intelectual": {
            "objetivo": "Maestría Global",
            "descripcion": "Convertirse en un pensador (no seguidor) con competencia multilingüe para despliegue global"
        },
        "afectivo_emocional": {
            "objetivo": "Liderazgo de Carácter",
            "descripcion": "Integrar código ético de Spider-Man (bondad a pesar del sufrimiento). Ser pilar de apoyo en la comunidad."
        },
        "ocupacional": {
            "objetivo": "Libertad Económica",
            "descripcion": "Usar beca y conocimiento para asegurar acceso a carrera elegida. Autonomía de decisiones (5 años vs. 50)."
        }
    },
    
    # Arquetipos Heroicos
    "arquetipos": {
        "iron_man": "La inteligencia como arma. El ingenio ante la adversidad.",
        "batman": "Disciplina sin superpoderes. Preparación meticulosa.",
        "spider_man": "Bondad a pesar del sufrimiento. Responsabilidad absoluta.",
        "flash": "Velocidad de adaptación. Optimismo imparable."
    },
    
    # Ingeniería Emocional
    "ingenieria_emocional": {
        "paradigma": "No soy un reactor emocional. Soy un arquitecto de respuestas.",
        "metodologia": "Kaizen - Mejora continua del 1% diario",
        "formula": "365 días × 1% de mejora = Transformación exponencial"
    }
}


# ============================================
# FUNCIONES DE ANÁLISIS
# ============================================

def analizar_falla_critica():
    """
    Función que analiza la Falla Crítica (Falta Tipo II) y 
    genera el diagnóstico del Plan de Recuperación.
    
    Demuestra el pensamiento analítico sistemático aplicado
    a situaciones de crisis personal.
    """
    
    print("=" * 70)
    print("ANÁLISIS DE FALLA CRÍTICA - S.O.P. V. 2.0")
    print("=" * 70)
    print()
    
    # Definición de la Falla
    falla = {
        "tipo": "Falta Tipo II - Falla de Carácter",
        "descripcion": "Falta de respeto manifiesta hacia figura de autoridad familiar",
        "detonante": "Conflicto escalado por falta de autocontrol emocional",
        "consecuencias": [
            "Amenaza de suspensión de beneficios académicos (beca)",
            "Ruptura temporal de confianza familiar",
            "Riesgo a la estabilidad del proyecto de vida a largo plazo"
        ]
    }
    
    print("🔴 DIAGNÓSTICO DE LA FALLA:")
    print(f"   Tipo: {falla['tipo']}")
    print(f"   Descripción: {falla['descripcion']}")
    print(f"   Detonante: {falla['detonante']}")
    print()
    print("   Consecuencias Identificadas:")
    for i, consecuencia in enumerate(falla['consecuencias'], 1):
        print(f"   {i}. {consecuencia}")
    
    print()
    print("-" * 70)
    print("🔧 ANÁLISIS CAUSA-RAÍZ (Root Cause Analysis):")
    print("-" * 70)
    
    causas_raiz = {
        "primaria": "Código V. 1.0 - Sistema de protección emocional obsoleto",
        "secundarias": [
            "Uso de la grosería como mecanismo de defensa",
            "Falta de práctica en gestión de emociones intensas",
            "Ausencia de la aplicación de Dicotomía del Control en el momento crítico"
        ],
        "factores_agravantes": [
            "Acumulación de estrés académico no procesado",
            "Conflictos relacionales previos no resueltos"
        ]
    }
    
    print(f"   Causa Primaria: {causas_raiz['primaria']}")
    print()
    print("   Causas Secundarias:")
    for i, causa in enumerate(causas_raiz['secundarias'], 1):
        print(f"   {i}. {causa}")
    print()
    print("   Factores Agravantes:")
    for i, factor in enumerate(causas_raiz['factores_agravantes'], 1):
        print(f"   {i}. {factor}")
    
    print()
    print("-" * 70)
    print("✅ PLAN DE RECUPERACIÓN:")
    print("-" * 70)
    
    plan_recuperacion = {
        "fase_1_inmediata": {
            "accion": "Disculpa Estratégica",
            "plazo": "24-48 horas",
            "detalles": [
                "Reconocimiento explícito de la falta",
                "Asumir responsabilidad sin justificaciones",
                "Expresar compromiso con el cambio de comportamiento"
            ]
        },
        "fase_2_corto_plazo": {
            "accion": "Demostración de Cambio",
            "plazo": "1-3 meses",
            "detalles": [
                "Liquidación de deuda académica (PRIORIDAD: Matemáticas)",
                "Implementación visible de nueva conducta (Código V. 2.0)",
                "Establecimiento de comunicación transparente y respetuosa"
            ]
        },
        "fase_3_sostenibilidad": {
            "accion": "Prevención de Recaídas",
            "plazo": "Permanente",
            "detalles": [
                "Práctica diaria de Dicotomía del Control",
                "Tiempo de reflexión ante situaciones de alto estrés",
                "Sistema de alertas para detectar patrones del Código V. 1.0"
            ]
        }
    }
    
    for fase, contenido in plan_recuperacion.items():
        print(f"\n   {fase.upper().replace('_', ' ')}:")
        print(f"   → Acción: {contenido['accion']}")
        print(f"   → Plazo: {contenido['plazo']}")
        print(f"   → Detalles:")
        for detalle in contenido['detalles']:
            print(f"      • {detalle}")
    
    print()
    print("=" * 70)
    print("📊 MÉTRICAS DE ÉXITO:")
    print("=" * 70)
    
    metricas = {
        "academicas": "Recuperación de calificaciones a nivel > 8.0",
        "relacionales": "Restauración de confianza familiar (evaluación subjetiva)",
        "conductuales": "0 incidentes de falta de respeto en 3 meses consecutivos",
        "economicas": "Preservación de la beca académica"
    }
    
    for categoria, metrica in metricas.items():
        print(f"   • {categoria.capitalize()}: {metrica}")
    
    print()
    print("=" * 70)
    print("💡 LECCIÓN APRENDIDA:")
    print("=" * 70)
    print("""
   La Falla Tipo II no es un defecto del sistema, sino una ACTUALIZACIÓN NECESARIA.
   
   Cada error es data. Cada crisis es una oportunidad para fortalecer el código.
   El verdadero fracaso no es caer, sino permanecer caído.
   
   "Si vis pacem, para bellum" - La paz requiere preparación.
   La disciplina no es castigo, es el firewall que protege tu futuro.
   
   S.O.P. V. 2.0 >> Actualización en proceso...
   """)
    print("=" * 70)
    print()


def mostrar_resumen_proyecto():
    """
    Función que imprime un resumen ejecutivo del proyecto de vida.
    """
    print("\n" + "=" * 70)
    print("RESUMEN EJECUTIVO - S.O.P. V. 2.0")
    print("=" * 70)
    
    print(f"\n📌 ESTUDIANTE: Grado {PROYECTO_DE_VIDA['metadata']['estudiante']['grado']} | Edad: {PROYECTO_DE_VIDA['metadata']['estudiante']['edad']} años")
    print(f"🎯 LEMA: {PROYECTO_DE_VIDA['kernel']['lema_principal']}")
    print(f"   ({PROYECTO_DE_VIDA['kernel']['traduccion']})")
    
    print("\n⚙️ FILOSOFÍA CENTRAL:")
    for principio in PROYECTO_DE_VIDA['kernel']['principios']:
        print(f"   • {principio}")
    
    print("\n🎯 PRIORIDADES CORTO PLAZO:")
    for aspecto, datos in PROYECTO_DE_VIDA['metas_corto_plazo'].items():
        if datos.get('prioridad') == 'CRÍTICA':
            print(f"   🔴 {aspecto.upper()}: {datos['objetivo']}")
    
    print("\n🦸 ARQUETIPOS INTEGRADOS:")
    for heroe, descripcion in PROYECTO_DE_VIDA['arquetipos'].items():
        print(f"   • {heroe.replace('_', ' ').upper()}: {descripcion}")
    
    print("\n" + "=" * 70)
    print("Estado del Sistema: EN_EJECUCION ✅")
    print("=" * 70 + "\n")


def mostrar_menu():
    """
    Función que muestra el menú interactivo del sistema.
    """
    print("\n" + "=" * 70)
    print("🖥️  MENÚ PRINCIPAL - S.O.P. V. 2.0")
    print("=" * 70)
    print("\n[1] Ver Resumen del Proyecto")
    print("[2] Analizar Falla Crítica")
    print("[3] Ver Metas por Aspecto")
    print("[4] Ver Arquetipos Heroicos")
    print("[5] Ver Algoritmo de Resiliencia")
    print("[0] Salir del Sistema")
    print("\n" + "=" * 70)


def ver_metas_aspecto():
    """
    Función interactiva para ver metas por aspecto específico.
    """
    print("\n" + "=" * 70)
    print("📊 SELECCIÓN DE ASPECTO")
    print("=" * 70)
    print("\n[1] Intelectual")
    print("[2] Afectivo/Emocional")
    print("[3] Ocupacional")
    print("[4] Espiritual")
    print("[5] Ver Todos")
    print("[0] Volver al menú principal")
    
    try:
        opcion = input("\n👉 Selecciona una opción: ").strip()
        
        aspectos_map = {
            "1": "intelectual",
            "2": "afectivo_emocional",
            "3": "ocupacional",
            "4": "espiritual"
        }
        
        if opcion == "0":
            return
        elif opcion == "5":
            for aspecto in ["intelectual", "afectivo_emocional", "ocupacional", "espiritual"]:
                mostrar_metas_de_aspecto(aspecto)
        elif opcion in aspectos_map:
            mostrar_metas_de_aspecto(aspectos_map[opcion])
        else:
            print("\n❌ Opción no válida.")
    except Exception as e:
        print(f"\n❌ Error: {e}")


def mostrar_metas_de_aspecto(aspecto):
    """
    Muestra las metas de un aspecto específico en los 3 plazos.
    """
    print("\n" + "=" * 70)
    print(f"📋 METAS DEL ASPECTO: {aspecto.upper().replace('_', ' ')}")
    print("=" * 70)
    
    # Corto Plazo
    if aspecto in PROYECTO_DE_VIDA['metas_corto_plazo']:
        datos = PROYECTO_DE_VIDA['metas_corto_plazo'][aspecto]
        print(f"\n⚡ CORTO PLAZO (1-3 meses) - Prioridad: {datos.get('prioridad', 'N/A')}")
        print(f"   Objetivo: {datos['objetivo']}")
        print("   Acciones:")
        for accion in datos['acciones']:
            print(f"   • {accion}")
    
    # Medio Plazo
    if aspecto in PROYECTO_DE_VIDA['metas_medio_plazo']:
        datos = PROYECTO_DE_VIDA['metas_medio_plazo'][aspecto]
        print(f"\n🔥 MEDIO PLAZO (6-12 meses)")
        print(f"   Objetivo: {datos['objetivo']}")
        print("   Acciones:")
        for accion in datos['acciones']:
            print(f"   • {accion}")
    
    # Largo Plazo
    if aspecto in PROYECTO_DE_VIDA['metas_largo_plazo']:
        datos = PROYECTO_DE_VIDA['metas_largo_plazo'][aspecto]
        print(f"\n🎯 LARGO PLAZO (1-3 años)")
        print(f"   Objetivo: {datos['objetivo']}")
        print(f"   Descripción: {datos['descripcion']}")
    
    print("\n" + "=" * 70)


def ver_arquetipos():
    """
    Muestra los arquetipos heroicos integrados.
    """
    print("\n" + "=" * 70)
    print("🦸 ARQUETIPOS HEROICOS INTEGRADOS")
    print("=" * 70)
    
    for heroe, descripcion in PROYECTO_DE_VIDA['arquetipos'].items():
        print(f"\n⭐ {heroe.replace('_', ' ').upper()}")
        print(f"   {descripcion}")
    
    print("\n💡 Ingeniería Emocional:")
    print(f"   {PROYECTO_DE_VIDA['ingenieria_emocional']['paradigma']}")
    print(f"\n📈 {PROYECTO_DE_VIDA['ingenieria_emocional']['metodologia']}")
    print(f"   {PROYECTO_DE_VIDA['ingenieria_emocional']['formula']}")
    
    print("\n" + "=" * 70)


def ver_algoritmo():
    """
    Muestra el algoritmo de resiliencia.
    """
    print("\n" + "=" * 70)
    print("⚙️  ALGORITMO DE RESILIENCIA")
    print("=" * 70)
    print(PROYECTO_DE_VIDA['kernel']['algoritmo_resiliencia'])
    print("\n💡 Este algoritmo representa mi respuesta sistemática ante adversidades.")
    print("=" * 70)


# ============================================
# EJECUCIÓN PRINCIPAL CON MENÚ INTERACTIVO
# ============================================

def main():
    """
    Función principal con menú interactivo.
    """
    print("\n" + "🚀" * 35)
    print("   INICIANDO S.O.P. V. 2.0 - SISTEMA OPERATIVO PERSONAL")
    print("🚀" * 35)
    
    while True:
        mostrar_menu()
        
        try:
            opcion = input("\n👉 Selecciona una opción: ").strip()
            
            if opcion == "1":
                mostrar_resumen_proyecto()
            elif opcion == "2":
                analizar_falla_critica()
            elif opcion == "3":
                ver_metas_aspecto()
            elif opcion == "4":
                ver_arquetipos()
            elif opcion == "5":
                ver_algoritmo()
            elif opcion == "0":
                print("\n" + "=" * 70)
                print("💾 Cerrando S.O.P. V. 2.0...")
                print("💪 'La disciplina es el puente entre las metas y los logros.'")
                print("🎯 ¡Sigue construyendo tu mejor versión!")
                print("=" * 70 + "\n")
                break
            else:
                print("\n❌ Opción no válida. Por favor selecciona una opción del menú.")
            
            # Pausa para que el usuario pueda leer
            input("\n⏸️  Presiona ENTER para continuar...")
            
        except KeyboardInterrupt:
            print("\n\n💾 Sistema interrumpido por el usuario.")
            print("🎯 ¡Hasta pronto!")
            break
        except Exception as e:
            print(f"\n❌ Error inesperado: {e}")
            input("\n⏸️  Presiona ENTER para continuar...")


if __name__ == "__main__":
    main()