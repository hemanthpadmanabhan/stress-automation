//properties([parameters([choice(choices:'boost\ndebug\naggregator',description: 'Select build type to build',name:'build')])])
properties([parameters([[$class: 'ChoiceParameter',
choiceType: 'PT_SINGLE_SELECT', filterLength: 1, filterable: false, name: 'Configuration',description: 'Select Configuration ',randomName: 'choice-parameter-689668596217089',
script: [$class: 'GroovyScript', fallbackScript: [classpath: [], oldScript: '', sandbox: true, script: ''],
script: [classpath: [], oldScript: '', sandbox: true, script: 'return ["debug", "release"]']]],
[$class: 'ChoiceParameter', choiceType: 'PT_MULTI_SELECT', filterLength: 1, filterable: true,
name: 'Components',description: 'Select Components type to build', randomName: 'choice-parameter-689668597266713',
script: [$class: 'GroovyScript', fallbackScript: [classpath: [], oldScript: '', sandbox: true, script: ''], 
script: [classpath: [], oldScript: '', sandbox: true, script: 'return ["aggregator","asdp","boost","ccrt","cctrl","cfgmgr","cilkabi","client","clienthelpers","clpt","collectdlg","collectunits","commhelpers","commondlg","compiler_libs","confcli","configs","confolh","confpostinstalldocs","confpreinstalldocs","confsamplecode","cpil","cs_eil","cs_gui_plug","curl","dbghelp","dblite","devutil","dia","dnclrprof","eil","featurestat","file_finder","formatter","gahelper","ged","gen_helpers","gtpin-parts","gui_ut_api","idvc_base","idvc_frw","idvc_graph","idvc_gridctl","idvc_propgrid","idvc_wx","iga","initdqtests","ism","level_zero","libunwind","libxml","libxslt","log4cplus","lpd","memorychecker","mrtehelpers","mrtesym","msngr","msngrext","msngrgui","panes","pdrdiff ","pin_parts ","pmeminsp","qfagent ","qfagentcrashanalyzer ","qfagentfeedback ","qfagentgui ","qfagentminidump ","rdmgr ","reporter ","runtool ","signing ","smip ","source_view ","sqlite ","stackwalk ","stripchartctrl","sys_check ","tbb ","tc_ ","tc_engine ","tcktests ","tctestdrivers ","threadchecker ","ts_cantua_cli_dq ","ts_cantua_cli_dq_lin ","ts_cantua_he_gui_dq ","ts_cantua_rcat_perf ","ts_common ","ts_cs_helpers ","ts_engine ","ts_msaa ","ts_panes ","ts_ut ","ts_vsautomation ","tsautomation ","tscsdmperf  ","tsguiengine ","tssourceview ","tswrappers ","tut ","userapi ","viewer ","vssdk ","wx_helpers ","wxwidgets ","xed ","xpti ","zlib "]']]]])])



currentBuild.displayName=currentBuild.number+"-# $params.Configuration component:: $params.Components"

pipeline {
    agent {label 'bcp-node'}
    environment{
        http_proxy = 'http://proxy-dmz.intel.com:912'
        https_proxy = 'http://proxy-dmz.intel.com:912'
        no_proxy  = 'localhost,127.0.0.1,intel.com,.intel.com'
        LC_ALL = 'en_US.UTF-8'
        LANG = 'en_US.UTF-8'
        LANGUAGE = 'en_US.UTF-8'
        COMPONENT_NAME = "${params.Components.replace(','," ")}"
	    //component=COMPONENT_NAME.replace(','," ")
        EMAIL_TO = 'surendrax.reddy.chejerla@intel.com,mahenrdax.naik.megavath@intel.com,hemanth.padmanabhan@intel.com,srinivas.murthy.rangarao@intel.com,narendra.singh@intel.com,madhurax.mahajan@intel.com,vishalx.kumar.kompelly@intel.com,naveenx.kandula@intel.com'

    }    
    stages {
	        stage('Checking Parameters') {
	 steps {
	 script{
		 
				if(params.Components.isEmpty()){
				timeout(time:30, unit:'SECONDS') {
					//result="${currentBuild.currentResult}"
		input message: 'This build requires parameters , can you please check one of the parameters and rerun the job ?'
			// currentBuild.result = 'ABORTED'
                        //error("parameters is empty")

}
			

				}
	 }	
			}
	}
        stage('Checkout') {
            steps{
            script{
           // checkout([$class: 'GitSCM',branches: [[name: '*/master']],doGenerateSubmoduleConfigurations: false,extensions: [[$class: 'RelativeTargetDirectory', relativeTargetDir: 'testjob2']],submoduleCfg: [],userRemoteConfigs: [[credentialsId: '53d8baf0-c5fb-42db-8d45-d0aa776a43a8', url: 'https://github.com/intel-innersource/applications.analyzers.inspector.git']]]) 
            checkout([$class: 'GitSCM',branches: [[name: 'v0.11.0.31']],doGenerateSubmoduleConfigurations: false,extensions: [[$class: 'RelativeTargetDirectory', relativeTargetDir: 'parts']],submoduleCfg: [],userRemoteConfigs: [[credentialsId: '53d8baf0-c5fb-42db-8d45-d0aa776a43a8', url: 'https://github.com/intel-innersource/applications.analyzers.infrastructure.parts.git']]]) 
            checkout([$class: 'GitSCM',branches: [[name: 'v0.11.0.31']],doGenerateSubmoduleConfigurations: false,extensions: [[$class: 'RelativeTargetDirectory', relativeTargetDir: 'parts-site']],submoduleCfg: [],userRemoteConfigs: [[credentialsId: '53d8baf0-c5fb-42db-8d45-d0aa776a43a8', url: 'https://github.com/intel-innersource/applications.analyzers.infrastructure.parts-site.git']]])
            checkout([$class: 'GitSCM',branches: [[name: '*/master']],doGenerateSubmoduleConfigurations: false,extensions: [[$class: 'RelativeTargetDirectory', relativeTargetDir: 'parts-site/pieces/infrascripts']],submoduleCfg: [],userRemoteConfigs: [[credentialsId: '53d8baf0-c5fb-42db-8d45-d0aa776a43a8', url: 'https://github.com/intel-innersource/applications.analyzers.infrastructure.infrascripts.git']]])

            echo 'Cloning completed --1............................'
        }
        }
        }
  
        stage ('Build') {
		
            steps {
			  
		    sh  "scons -j8 --bcfg=$params.Configuration do_cross=false groups=cli,gui ${env.COMPONENT_NAME}"
			  	//sh 'scons package all'
			    //sh 'scons build-config=debug package all'
			  	//sh 'scons --build-config=release package all'

                           echo 'Build is  completed --2............................'
                  }
             }
        
        stage('Test') {
            steps {
                echo 'Testing..'
                sh '''
            echo 'Test is  completed --3............................'
                '''
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
                sh '''
                '''
            }
        }
}
	post {
        failure {
		 mail to: "${env.EMAIL_TO}", from : 'noreply@intel.com',
                subject: "${currentBuild.currentResult}: ${env.JOB_NAME}",
                body: "Build failed - \"${env.JOB_NAME}\" build no: ${env.BUILD_NUMBER} Component Name: ${env.COMPONENT_NAME} \n\nView the log at:\n ${env.BUILD_URL}\n\nBlue Ocean:\n${env.RUN_DISPLAY_URL}"
        }
    success{
            mail to: "${env.EMAIL_TO}", from : 'noreply@intel.com',
                subject: "${currentBuild.currentResult}: ${env.JOB_NAME}", 
                body: "Build Successful - \"${env.JOB_NAME}\" build no: ${env.BUILD_NUMBER} Component Name: ${env.COMPONENT_NAME} \n\nView the log at:\n ${env.BUILD_URL}\n\nBlue Ocean:\n${env.RUN_DISPLAY_URL}"
        }
        aborted{
            mail to: "${env.EMAIL_TO}", from : 'noreply@intel.com',
                subject: "${currentBuild.currentResult}: ${env.JOB_NAME}", 
                body: "Build was aborted - \"${env.JOB_NAME}\" build no: ${env.BUILD_NUMBER} Component Name: ${env.COMPONENT_NAME} \n\nView the log at:\n ${env.BUILD_URL} \n\nBlue Ocean:\n${env.RUN_DISPLAY_URL}"
        }
    }

}
